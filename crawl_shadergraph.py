#!/usr/bin/env python3
"""
ShaderGraph Node Names Extractor using Crawl4AI

Usage:
    python3 crawl_shadergraph.py [--config extract_llm.yml] [--provider PROVIDER] [--api-token TOKEN] [--instruction INSTRUCTION]

This script crawls the Unity ShaderGraph Node Library page and extracts nodes into a normalized
Crawl Mode JSON structure (topics -> categories -> nodes).

It prefers configuration from `extract_llm.yml` in the repo root but accepts CLI overrides.
"""

import os
import argparse
import asyncio
import json
from typing import List, Optional
from pydantic import BaseModel, Field

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig
from crawl4ai import LLMExtractionStrategy

try:
    import yaml
except Exception:
    yaml = None

try:
    from dotenv import load_dotenv
    load_dotenv()  # load .env from repo root if present
except Exception:
    # python-dotenv not installed; rely on existing environment
    pass


class ShaderGraphNode(BaseModel):
    name: str = Field(description="The name of the ShaderGraph node")


class ShaderGraphNodeList(BaseModel):
    nodes: List[ShaderGraphNode]


def load_config(path: Optional[str]):
    if not path:
        return None
    if not yaml:
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def resolve_provider_and_token(config_path: Optional[str], provider_override: Optional[str], token_override: Optional[str]):
    # CLI overrides take precedence
    if provider_override or token_override:
        return token_override, provider_override

    # Try config file
    if config_path:
        cfg = load_config(config_path)
        if cfg:
            prov = cfg.get('provider')
            # Do NOT read API tokens from YAML. Prefer environment variables.
            if prov:
                # Even if the YAML contains the provider, check environment vars for tokens
                openai_key = os.getenv('OPENAI_API_KEY')
                if openai_key:
                    return openai_key, prov
                anthropic_key = os.getenv('ANTHROPIC_API_KEY')
                if anthropic_key:
                    return anthropic_key, prov
                hf = os.getenv('HUGGINGFACE_API_TOKEN')
                if hf:
                    return hf, prov
                # No token in environment: return provider only
                return None, prov

    # Fallback env vars
    openai_key = os.getenv('OPENAI_API_KEY')
    if openai_key:
        return openai_key, 'openai/gpt-4o-mini'
    anthropic_key = os.getenv('ANTHROPIC_API_KEY')
    if anthropic_key:
        return anthropic_key, 'anthropic/claude-3-haiku-20240307'
    hf = os.getenv('HUGGINGFACE_API_TOKEN')
    if hf:
        return hf, 'huggingface/microsoft/DialoGPT-medium'

    # Default to local
    return None, 'ollama/llama2'


async def run_crawl(url: str, api_token: Optional[str], provider: str, instruction: Optional[str]):
    # Configure LLM
    if api_token:
        llm_config = LLMConfig(provider=provider, api_token=api_token)
    else:
        llm_config = LLMConfig(provider=provider)

    # Default instruction if none provided
    if not instruction:
        # Try to load from extract_llm.yml in repo root
        repo_cfg = load_config('extract_llm.yml')
        if repo_cfg:
            instruction = repo_cfg.get('instruction')

    if not instruction:
        instruction = (
            "Return a strict JSON array of topic objects. Each topic must have 'topic' (string) and 'categories' (array). "
            "Each category must have 'category' (string) and 'nodes' (array of node-name strings)."
        )

    # JSON schema that matches the Crawl Mode structure we expect from the LLM
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
                "categories": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "category": {"type": "string"},
                            "nodes": {"type": "array", "items": {"type": "string"}}
                        },
                        "required": ["category", "nodes"]
                    }
                }
            },
            "required": ["topic", "categories"]
        }
    }

    llm_strategy = LLMExtractionStrategy(
        llm_config=llm_config,
        schema=schema,
        extraction_type='schema',
        instruction=instruction,
        chunk_token_threshold=2000,
        overlap_rate=0.0,
        apply_chunking=True,
        input_format='markdown',
        extra_args={'temperature': 0.0, 'max_tokens': 3000},
        verbose=True
    )

    crawl_cfg = CrawlerRunConfig(
        extraction_strategy=llm_strategy,
        cache_mode=CacheMode.BYPASS
    )

    browser_cfg = BrowserConfig(headless=True)

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        result = await crawler.arun(url=url, config=crawl_cfg)

    if not result.success:
        raise RuntimeError(f"Crawl failed: {result.error_message}")

    # Parse extracted content
    try:
        extracted = json.loads(result.extracted_content)
    except Exception:
        # fallback: try markdown
        extracted = result.extracted_content

    # Normalize into Crawl Mode structure
    normalized = []
    if isinstance(extracted, list):
        for topic_entry in extracted:
            if not isinstance(topic_entry, dict):
                continue
            topic = topic_entry.get('topic')
            cats = topic_entry.get('categories') or []
            norm_cats = []
            for c in cats:
                if not isinstance(c, dict):
                    continue
                cat_name = c.get('category') or topic
                nodes = c.get('nodes') or []
                nodes = [n.strip() for n in nodes if isinstance(n, str) and n.strip()]
                if nodes:
                    norm_cats.append({'category': cat_name, 'nodes': nodes})
            if norm_cats:
                normalized.append({'topic': topic, 'categories': norm_cats})

    # Write outputs
    with open('shadergraph_nodes.json', 'w', encoding='utf-8') as f:
        json.dump({'url': url, 'extraction': extracted}, f, indent=2, ensure_ascii=False)

    with open('shadergraph_crawlmode.json', 'w', encoding='utf-8') as f:
        json.dump(normalized, f, indent=2, ensure_ascii=False)

    # Also return summary
    return normalized


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='extract_llm.yml', help='Path to YAML config')
    parser.add_argument('--provider', type=str, default=None, help='LLM provider override')
    parser.add_argument('--api-token', type=str, default=None, help='LLM API token override')
    parser.add_argument('--instruction', type=str, default=None, help='LLM instruction override')
    args = parser.parse_args()

    url = 'https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node-Library.html'

    api_token, provider = resolve_provider_and_token(args.config, args.provider, args.api_token)

    print('Resolved provider:', provider)
    print('API token present:', bool(api_token))
    print('Instruction override present:', bool(args.instruction))

    # Basic validation: if provider is a hosted provider that requires a key, ensure we have one
    hosted_prefixes = ['openai/', 'anthropic/', 'huggingface/']
    if any(provider.startswith(p) for p in hosted_prefixes) and not api_token:
        print('\n\n❌ Missing API token for hosted LLM provider:', provider)
        print('Please set the appropriate environment variable (e.g. OPENAI_API_KEY) or pass --api-token')
        raise SystemExit(1)

    normalized = asyncio.run(run_crawl(url, api_token, provider, args.instruction))

    print('\nCrawl Mode topics found:', len(normalized))
    for t in normalized:
        print('-', t.get('topic'), '->', len(t.get('categories', [])), 'categories')


if __name__ == '__main__':
    main()