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
    """Resolve the LLM provider and API token.

    Returns a tuple: (api_token or None, provider str, provider_source)
    provider_source is one of: 'cli', 'config', 'env', 'fallback'
    """
    # CLI overrides take precedence
    if provider_override or token_override:
        return token_override, provider_override, 'cli'

    # If a config file provides a provider name, use it (tokens still come from env)
    if config_path:
        cfg = load_config(config_path)
        if cfg:
            prov = cfg.get('provider')
            if prov:
                # Prefer environment variables for tokens (never read tokens from YAML)
                openai_key = os.getenv('OPENAI_API_KEY')
                if openai_key:
                    return openai_key, prov, 'config'
                anthropic_key = os.getenv('ANTHROPIC_API_KEY')
                if anthropic_key:
                    return anthropic_key, prov, 'config'
                hf = os.getenv('HUGGINGFACE_API_TOKEN')
                if hf:
                    return hf, prov, 'config'
                # No token in environment: return provider only (from config)
                return None, prov, 'config'

    # Fallback env vars
    openai_key = os.getenv('OPENAI_API_KEY')
    if openai_key:
        return openai_key, 'openai/gpt-4.1', 'env'
    anthropic_key = os.getenv('ANTHROPIC_API_KEY')
    if anthropic_key:
        return anthropic_key, 'anthropic/claude-3-haiku-latest', 'env'
    hf = os.getenv('HUGGINGFACE_API_TOKEN')
    if hf:
        return hf, 'huggingface/microsoft/DialoGPT-medium', 'env'

    # Default to local
    return None, 'ollama/llama2', 'fallback'


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

    # Return both the raw extracted content and normalized Crawl Mode structure
    return extracted, normalized


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('crawl_yaml', type=str, nargs='?', help='Path to a single crawl YAML file (required)')
    parser.add_argument('--config', type=str, default='extract_llm.yml', help='Path to YAML config for provider/instruction defaults')
    parser.add_argument('--provider', type=str, default=None, help='LLM provider override')
    parser.add_argument('--api-token', type=str, default=None, help='LLM API token override')
    parser.add_argument('--instruction', type=str, default=None, help='LLM instruction override')
    parser.add_argument('--save-raw', action='store_true', help='Write raw extraction output with metadata to <prefix>_raw.json')
    parser.add_argument('--content', action='store_true', help='Use LLM to capture additional content (descriptions) per node')
    args = parser.parse_args()

    # Require a single YAML argument; print help if missing
    if not args.crawl_yaml:
        parser.print_help()
        raise SystemExit(1)

    if not os.path.isfile(args.crawl_yaml):
        print('Crawl YAML not found:', args.crawl_yaml)
        raise SystemExit(1)

    cfg = load_config(args.crawl_yaml)
    if not cfg:
        print('Failed to load YAML config or file empty:', args.crawl_yaml)
        raise SystemExit(1)

    url = cfg.get('url')
    # support both legacy 'instruction' and the newer 'structure_instruction'
    structure_instruction = cfg.get('structure_instruction') or cfg.get('instruction')
    content_instruction = cfg.get('content_instruction')
    instruction = structure_instruction or args.instruction
    output_prefix = cfg.get('output_prefix') or cfg.get('name') or os.path.splitext(os.path.basename(args.crawl_yaml))[0]

    # Determine provider and token
    cfg_provider = cfg.get('provider')
    if args.provider or args.api_token:
        # explicit CLI overrides
        api_token = args.api_token
        provider = args.provider
        provider_source = 'cli'
    elif cfg_provider:
        # provider specified in the crawl YAML; prefer environment tokens
        provider = cfg_provider
        api_token = None
        if provider.startswith('openai/'):
            api_token = os.getenv('OPENAI_API_KEY')
        elif provider.startswith('anthropic/'):
            api_token = os.getenv('ANTHROPIC_API_KEY')
        elif provider.startswith('huggingface/'):
            api_token = os.getenv('HUGGINGFACE_API_TOKEN')
        # fallback: check common envs in order
        if not api_token:
            api_token = os.getenv('OPENAI_API_KEY') or os.getenv('ANTHROPIC_API_KEY') or os.getenv('HUGGINGFACE_API_TOKEN')
        provider_source = 'config'
    else:
        api_token, provider, provider_source = resolve_provider_and_token(args.config, args.provider, args.api_token)

    print('\nRunning crawl for:', url)
    print('Resolved provider:', provider)
    print('Provider source:', provider_source)
    print('API token present:', bool(api_token))

    # Basic validation: if provider is a hosted provider that requires a key, ensure we have one
    hosted_prefixes = ['openai/', 'anthropic/', 'huggingface/']
    use_dom_fallback = False
    if any(provider.startswith(p) for p in hosted_prefixes) and not api_token:
        # If the user requested --content, we can still proceed using DOM-based extraction + heuristics
        if args.content:
            print('\n\n⚠️ No API token found for hosted LLM provider:', provider)
            print('Falling back to DOM-based extraction and heuristics for content enrichment (no LLM will be used).')
            use_dom_fallback = True
        else:
            print('\n\n❌ Missing API token for hosted LLM provider:', provider)
            if provider_source == 'config':
                print(f"Provider '{provider}' was selected from the config file: {args.config}")
                print('No API token was found in your environment. Please set the appropriate environment variable:')
                if provider.startswith('openai/'):
                    print('  export OPENAI_API_KEY="<your-key>"')
                elif provider.startswith('anthropic/'):
                    print('  export ANTHROPIC_API_KEY="<your-key>"')
                elif provider.startswith('huggingface/'):
                    print('  export HUGGINGFACE_API_TOKEN="<your-token>"')
                print('Or re-run with --api-token <TOKEN> to provide it directly.')
            else:
                print('Please set the appropriate environment variable (e.g. OPENAI_API_KEY) or pass --api-token')
            raise SystemExit(1)

    # Always run structure extraction first to get a canonical structure
    if use_dom_fallback:
        # perform DOM-based structure extraction from the index page
        try:
            import requests
            from bs4 import BeautifulSoup
            from urllib.parse import urljoin

            def build_normalized_from_index(index_url):
                resp = requests.get(index_url, timeout=12, headers={'User-Agent': 'crawl-cat/1.0'})
                resp.raise_for_status()
                soup = BeautifulSoup(resp.text, 'html.parser')
                # find sections by h2/h3 headings and collect following anchors
                categories = []
                last_heading = None
                for tag in soup.find_all(['h2', 'h3']):
                    heading = (tag.get_text(' ', strip=True) or '').strip()
                    if not heading:
                        continue
                    nodes = []
                    sib = tag.find_next_sibling()
                    scanned = 0
                    while sib and scanned < 200:
                        if getattr(sib, 'name', None) in ('h2', 'h3'):
                            break
                        # collect anchors within paragraphs and lists
                        for a in sib.find_all('a', href=True):
                            txt = (a.get_text() or '').strip()
                            href = a.get('href')
                            if txt and href and href.endswith('.html'):
                                nodes.append(txt)
                        sib = sib.find_next_sibling()
                        scanned += 1
                    if nodes:
                        categories.append({'category': heading, 'nodes': nodes})

                # if no categories found, fallback to gathering all .html anchors with texts
                if not categories:
                    anchors = []
                    for a in soup.find_all('a', href=True):
                        href = a.get('href')
                        txt = (a.get_text() or '').strip()
                        if href and href.endswith('.html') and txt and len(txt) > 2:
                            anchors.append(txt)
                    if anchors:
                        categories = [{'category': 'nodes', 'nodes': anchors}]

                topic = {'topic': 'OBJ Nodes', 'categories': categories}
                # return extracted_struct, normalized (both lists); metadata can be included in extracted if desired
                return [topic], [topic]

            extracted_struct, normalized = build_normalized_from_index(url)
        except Exception as e:
            raise RuntimeError(f'DOM fallback extraction failed: {e}')
    else:
        extracted_struct, normalized = asyncio.run(run_crawl(url, api_token, provider, instruction))

    # If saving raw, write the structure extraction raw output
    if args.save_raw:
        metadata = {
            'url': url,
            'provider': provider,
            'provider_source': provider_source,
            'instruction': instruction,
            'timestamp': __import__('datetime').datetime.utcnow().isoformat() + 'Z'
        }
        raw_out = f"{output_prefix}_raw.json"
        with open(raw_out, 'w', encoding='utf-8') as f:
            json.dump({'metadata': metadata, 'extraction': extracted_struct}, f, indent=2, ensure_ascii=False)

    # If content capture requested, run a second LLM extraction asking only for descriptions aligned to the structure
    descriptions_map = {}  # name -> description
    if args.content:
        # Build a content-only instruction that references the canonical structure
        # Flatten node names in order to provide the LLM with exact names to annotate
        structure_list = []
        for topic in normalized:
            for c in topic.get('categories', []):
                for n in c.get('nodes', []):
                    if isinstance(n, dict):
                        structure_list.append(n.get('name'))
                    else:
                        structure_list.append(n)

        # Compose content instruction: ask LLM to return same structure but nodes as objects with descriptions
        content_prompt_parts = []
        if content_instruction:
            content_prompt_parts.append(content_instruction.strip())
        else:
            content_prompt_parts.append(
                "For each node in the structure, return a short one-sentence description when available. "
                "Return a JSON array matching the same topic/category structure but nodes should be objects: {name, description}. "
                "If a description is not available, return an empty string for description."
            )

        # Provide the exact node list to avoid structural drift
        content_prompt_parts.append('\n\nHere is the canonical list of node names to annotate:')
        # List up to a reasonable limit to avoid huge prompts (but include all for accuracy)
        content_prompt_parts.append('\n' + json.dumps(structure_list, ensure_ascii=False))

        combined_content_instruction = "\n\n".join(content_prompt_parts)

        # Run LLM extraction for content
        extracted_content, normalized_content = asyncio.run(run_crawl(url, api_token, provider, combined_content_instruction))

        # Build a map from node name -> description from normalized_content
        if isinstance(normalized_content, list):
            for topic in normalized_content:
                for c in topic.get('categories', []):
                    for n in c.get('nodes', []):
                        if isinstance(n, dict):
                            nm = n.get('name')
                            desc = n.get('description') or ''
                            if nm:
                                descriptions_map[nm] = desc
                        elif isinstance(n, str):
                            # no description provided
                            descriptions_map[n] = ''

    # Now merge descriptions_map into the canonical normalized structure and run heuristics for missing ones
    # prepare main_soup for heuristics if needed
    main_soup = None
    if args.content:
        try:
            import requests
            from bs4 import BeautifulSoup
            main_soup = None
            try:
                resp = requests.get(url, timeout=8, headers={'User-Agent': 'crawl-cat/1.0'})
                resp.raise_for_status()
                main_soup = BeautifulSoup(resp.text, 'html.parser')
            except Exception:
                main_soup = None
        except Exception:
            main_soup = None

    # helper functions used for heuristic description extraction
    def get_soup(page_url):
        try:
            resp = requests.get(page_url, timeout=8, headers={'User-Agent': 'crawl-cat/1.0'})
            resp.raise_for_status()
            return BeautifulSoup(resp.text, 'html.parser')
        except Exception:
            return None

    def extract_meta_or_first_p(soup):
        if not soup:
            return None
        # meta description
        m = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'property': 'og:description'})
        if m and m.get('content'):
            return m.get('content').strip()
        # Try to find a paragraph immediately after the main header (h1, h2, or h3)
        for htag in ['h1', 'h2', 'h3']:
            h = soup.find(htag)
            if h:
                header_text = (h.get_text(' ', strip=True) or '').strip()
                # look for next paragraph sibling with meaningful text
                sib = h.find_next_sibling()
                scanned = 0
                while sib and scanned < 12:
                    if getattr(sib, 'name', None) == 'p':
                        txt = sib.get_text(' ', strip=True)
                        if txt:
                            # prefer paragraphs that are not identical to header and that contain more than just the name
                            if txt.strip().lower() != header_text.lower() and len(txt.strip()) >= 10:
                                return txt
                    sib = sib.find_next_sibling()
                    scanned += 1

        # fallback: first paragraph with meaningful text (avoid short index lines)
        for p in soup.find_all('p'):
            txt = p.get_text(' ', strip=True)
            if txt and len(txt) >= 10 and 'houdini' not in txt.lower():
                # avoid returning a paragraph that is only the node name
                # check nearby header to compare
                parent_header = None
                h = p.find_previous(['h1', 'h2', 'h3'])
                if h:
                    parent_header = (h.get_text(' ', strip=True) or '').strip()
                if parent_header and txt.strip().lower() == parent_header.lower():
                    continue
                return txt

        return None

    def find_on_page_description(main_soup, node_name):
        if not main_soup:
            return None, None
        # find links or elements that contain the node name
        # exact match links first
        node_lower = node_name.strip().lower()
        # try anchors
        for a in main_soup.find_all('a'):
            txt = (a.get_text() or '').strip()
            if not txt:
                continue
            if txt.lower() == node_lower or node_lower in txt.lower():
                # description candidate: title attr, sibling text, parent paragraph
                if a.get('title'):
                    return a.get('title').strip(), a.get('href')
                # next sibling
                ns = a.find_next_sibling()
                if ns and ns.get_text(strip=True):
                    return ns.get_text(' ', strip=True), a.get('href')
                # parent paragraph
                p = a.find_parent('p')
                if p and p.get_text(strip=True):
                    return p.get_text(' ', strip=True), a.get('href')
        # fallback: headings that match then following paragraph
        for htag in ['h1','h2','h3','h4','h5']:
            for h in main_soup.find_all(htag):
                if node_lower in (h.get_text() or '').lower():
                    # next paragraph
                    np = h.find_next_sibling('p')
                    if np and np.get_text(strip=True):
                        return np.get_text(' ', strip=True), None
        return None, None

    enriched = []
    for topic in normalized:
        cats = []
        for c in topic.get('categories', []):
            nodes = []
            for node in c.get('nodes', []):
                if isinstance(node, dict):
                    name = node.get('name')
                    desc = (node.get('description') or '').strip()
                else:
                    name = node
                    desc = ''

                # prefer description from LLM content pass
                if name in descriptions_map and descriptions_map[name]:
                    # treat descriptions equal to name (case-insensitive) as missing
                    candidate = (descriptions_map[name] or '').strip()
                    if candidate and candidate.lower() != (name or '').strip().lower():
                        desc = candidate
                    else:
                        desc = ''

                # fallback: heuristics only when no description
                if (not desc or (name and desc.strip().lower() == name.strip().lower())) and args.content and main_soup:
                    try:
                        d, link = find_on_page_description(main_soup, name)
                        # if candidate is just the node name, treat as missing and try the node page
                        if d and name and d.strip().lower() == name.strip().lower():
                            d = None
                        if not d and link:
                            from urllib.parse import urljoin
                            page_url = urljoin(url, link)
                            soup = get_soup(page_url)
                            d = extract_meta_or_first_p(soup)
                        if not d and main_soup:
                            # broader search
                            text_nodes = main_soup.find_all(string=lambda s: name.lower() in s.lower())
                            if text_nodes:
                                parent = None
                                for tn in text_nodes:
                                    p = tn.find_parent('p')
                                    if p and p.get_text(strip=True):
                                        parent = p
                                        break
                                if parent:
                                    d = parent.get_text(' ', strip=True)
                        if d:
                            if len(d) > 300:
                                d = d.split('\n')[0][:300].strip()
                            desc = d
                    except Exception:
                        pass

                nodes.append({'name': name, 'description': desc or ''})
            cats.append({'category': c.get('category'), 'nodes': nodes})
        enriched.append({'topic': topic.get('topic'), 'categories': cats})

    # write enriched output only if content requested
    if args.content:
        enriched_out = f"{output_prefix}_enriched.json"
        with open(enriched_out, 'w', encoding='utf-8') as f:
            json.dump(enriched, f, indent=2, ensure_ascii=False)

    print('\nCrawl Mode topics found:', len(normalized))
    for t in normalized:
        print('-', t.get('topic'), '->', len(t.get('categories', [])), 'categories')

    # write outputs with the output_prefix
    raw_out = f"{output_prefix}_raw.json"
    normalized_out = f"{output_prefix}.json"

    if args.save_raw:
        # include provenance metadata
        metadata = {
            'url': url,
            'provider': provider,
            'provider_source': provider_source,
            'instruction': instruction,
            'timestamp': __import__('datetime').datetime.utcnow().isoformat() + 'Z'
        }
        with open(raw_out, 'w', encoding='utf-8') as f:
            json.dump({'metadata': metadata, 'extraction': extracted}, f, indent=2, ensure_ascii=False)

    with open(normalized_out, 'w', encoding='utf-8') as f:
        json.dump(normalized, f, indent=2, ensure_ascii=False)

    # (enrichment already produced above when --content was requested)


if __name__ == '__main__':
    main()