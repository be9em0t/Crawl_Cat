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

# Review/approve flow removed: persistent cleanup - this script no longer supports --review/--review-file/--approve


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


# -- Module-level helpers (moved from main for reuse and testing)
def get_soup(page_url):
    try:
        import requests
        from bs4 import BeautifulSoup
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


def extract_text_by_selectors_from_soup(soup, selectors):
    if not soup:
        return None
    for sel in selectors or []:
        try:
            els = soup.select(sel)
        except Exception:
            els = []
        for e in els:
            txt = e.get_text(' ', strip=True)
            if txt and len(txt) > 5:
                return txt
    return None


def extract_by_dom_selectors(page_url, selectors):
    s = get_soup(page_url)
    return extract_text_by_selectors_from_soup(s, selectors)


def fallback_extract_structure_from_dom(page_url):
    """Attempt a light-weight DOM-only extraction to produce the minimal Crawl Mode structure.
    This is used as a fallback when LLM-based structure extraction returns nothing.
    """
    soup = get_soup(page_url)
    if not soup:
        return []

    # Prefer anchors that look like node links (heuristic for Houdini: '/nodes/obj/')
    anchors = soup.find_all('a')
    candidates = []
    for a in anchors:
        href = a.get('href') or ''
        txt = (a.get_text() or '').strip()
        if not txt or len(txt) < 2:
            continue
        # Heuristic: link target contains nodes/obj or looks like a node page
        href_low = href.lower()
        if 'nodes/obj' in href_low or '/nodes/obj/' in href_low:
            candidates.append(txt)
        # also accept generic /nodes/ links or any .html link that looks like a node page
        elif '/nodes/' in href_low or href_low.endswith('.html'):
            # avoid external links or anchors that are navigation
            if href_low.startswith('http') or href_low.startswith('/') or href_low.startswith('#') or href_low:
                # accept likely node names (title-case or contains space)
                if any(c.isupper() for c in txt[:3]) or ' ' in txt:
                    candidates.append(txt)

    # If none found, try finding anchors under an "All tags" heading or similar list
    if not candidates:
        for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5']):
            if 'all tags' in (h.get_text() or '').lower() or 'all nodes' in (h.get_text() or '').lower():
                sib = h.find_next_sibling()
                if sib:
                    for a in sib.select('a'):
                        txt = (a.get_text() or '').strip()
                        if txt and len(txt) > 1:
                            candidates.append(txt)
                break

    # Deduplicate preserving order
    seen = set()
    nodes = []
    for n in candidates:
        if n not in seen:
            seen.add(n)
            nodes.append(n)

    if not nodes:
        return []

    # Return a minimal normalized structure with a single topic/category
    return [{
        'topic': 'Houdini OBJ',
        'categories': [
            {'category': 'OBJ Nodes', 'nodes': nodes}
        ]
    }]


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


async def run_crawl(url: str, api_token: Optional[str], provider: str, instruction: Optional[str], params: Optional[dict] = None):
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

    # Allow YAML/CLI provided params to override defaults
    params = params or {}
    temperature = params.get('temperature', 0.0)
    max_tokens = params.get('max_tokens', 3000)
    chunk_token_threshold = params.get('chunk_token_threshold', 2000)
    apply_chunking = params.get('apply_chunking', True)
    overlap_rate = params.get('overlap_rate', 0.0)

    llm_strategy = LLMExtractionStrategy(
        llm_config=llm_config,
        schema=schema,
        extraction_type='schema',
        instruction=instruction,
        chunk_token_threshold=chunk_token_threshold,
        overlap_rate=overlap_rate,
        apply_chunking=apply_chunking,
        input_format=params.get('input_format', 'markdown'),
        extra_args={'temperature': temperature, 'max_tokens': max_tokens},
        verbose=params.get('verbose', True)
    )

    crawl_cfg = CrawlerRunConfig(
        extraction_strategy=llm_strategy,
        cache_mode=CacheMode.BYPASS
    )

    browser_cfg = BrowserConfig(headless=True)

    import time
    start = time.perf_counter()
    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        result = await crawler.arun(url=url, config=crawl_cfg)
    elapsed = time.perf_counter() - start

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

    # Build metrics: counts and any provider-reported usage if available
    counts = {
        'topics': 0,
        'categories': 0,
        'nodes': 0,
        'nodes_with_description': 0
    }
    if isinstance(normalized, list):
        counts['topics'] = len(normalized)
        for t in normalized:
            cats = t.get('categories', []) if isinstance(t, dict) else []
            counts['categories'] += len(cats)
            for c in cats:
                nodes = c.get('nodes', []) if isinstance(c, dict) else []
                counts['nodes'] += len(nodes)
                for n in nodes:
                    if isinstance(n, dict) and (n.get('description') or '').strip():
                        counts['nodes_with_description'] += 1

    # Try to extract provider token usage information if the crawler exposes it
    llm_usage = None
    # common attribute names that might appear on result objects
    for attr in ('usage', 'llm_usage', 'token_usage', 'stats'):
        if hasattr(result, attr):
            try:
                llm_usage = getattr(result, attr)
                break
            except Exception:
                llm_usage = None

    metrics = {
        'elapsed_s': elapsed,
        'counts': counts,
        'llm_usage': llm_usage
    }

    # Return both the raw extracted content, normalized structure, and metrics
    return extracted, normalized, metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('crawl_yaml', type=str, nargs='?', help='Path to a single crawl YAML file (required)')
    # NOTE: removed --config flag; the positional crawl YAML defines site-specific settings
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
    dom_discovery_instruction = cfg.get('dom_discovery_instruction')
    dom_selectors = cfg.get('dom_selectors') or {}
        # review/approve functionality removed - nothing to imply here
        # The args.approve and args.review have been removed as part of the cleanup.
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
        # No separate global config argument; resolve provider/token from env/CLI only
        api_token, provider, provider_source = resolve_provider_and_token(None, args.provider, args.api_token)

    print('\nRunning crawl for:', url)
    print('Resolved provider:', provider)
    print('Provider source:', provider_source)
    print('API token present:', bool(api_token))

    # Basic validation: if provider is a hosted provider that requires a key, ensure we have one
    hosted_prefixes = ['openai/', 'anthropic/', 'huggingface/']
    if any(provider.startswith(p) for p in hosted_prefixes) and not api_token:
        if args.content:
            print('\n\nExiting. LLM not available for hosted provider:', provider)
            raise SystemExit(1)
        else:
            print('\n\n❌ Missing API token for hosted LLM provider:', provider)
            if provider_source == 'config':
                print(f"Provider '{provider}' was selected from the crawl YAML: {args.crawl_yaml}")
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
    extracted_struct, normalized, struct_metrics = asyncio.run(run_crawl(url, api_token, provider, instruction, params=cfg.get('params')))

    # If LLM returned nothing useful, attempt a deterministic DOM-only fallback
    if (not normalized or len(normalized) == 0):
        try:
            dom_fallback = fallback_extract_structure_from_dom(url)
            if dom_fallback:
                print('\n[Fallback] Using DOM-only extraction as LLM returned no structure')
                normalized = dom_fallback
                # minimal struct_metrics for fallback
                struct_metrics = {'elapsed_s': 0.0, 'counts': {'topics': len(normalized), 'categories': sum(len(t.get('categories', [])) for t in normalized), 'nodes': sum(len(c.get('nodes', [])) for t in normalized for c in t.get('categories', [])), 'nodes_with_description': 0}}
        except Exception:
            pass

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
    # Optionally use dom_selectors for deterministic scraping
    dom_proposed = None
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

        # DOM discovery removed from automated flow. If you need dom_selectors, add them to the YAML manually.

        # Run LLM extraction for content (still useful to get names->description mapping)
        extracted_content, normalized_content, content_metrics = asyncio.run(run_crawl(url, api_token, provider, combined_content_instruction))

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
            main_soup = get_soup(url)
        except Exception:
            main_soup = None

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
                            # If dom_selectors provided, try deterministic extraction first
                            node_selectors = dom_selectors.get('node_page_selectors') if isinstance(dom_selectors, dict) else None
                            if node_selectors:
                                d = extract_by_dom_selectors(page_url, node_selectors)
                            if not d:
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
            # keep original behaviour: write the enriched list (tests expect a list)
            json.dump(enriched, f, indent=2, ensure_ascii=False)
        # write metrics to a separate file for backward compatibility
        metrics_out = f"{output_prefix}_enriched_metrics.json"
        try:
            with open(metrics_out, 'w', encoding='utf-8') as mf:
                json.dump(content_metrics, mf, indent=2, ensure_ascii=False)
        except Exception:
            pass

    # Review/approve flow removed. If you need to discover or approve dom_selectors, add them manually to the YAML

    print('\nCrawl Mode topics found:', len(normalized))
    for t in normalized:
        print('-', t.get('topic'), '->', len(t.get('categories', [])), 'categories')

    # Print extraction metrics summary for structure (counts only)
    try:
        cm = struct_metrics
        print('\nStructure extraction:')
        print('- elapsed (s):', round(cm.get('elapsed_s', 0.0), 2))
        cnts = cm.get('counts', {})
        print('- topics:', cnts.get('topics', 0), 'categories:', cnts.get('categories', 0), 'nodes:', cnts.get('nodes', 0))
        if cm.get('llm_usage'):
            print('- llm_usage:', cm.get('llm_usage'))
    except Exception:
        pass

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
    if args.content:
        try:
            # derive nodes_with_description from the enriched data we just built
            nd_desc = 0
            total_nodes = 0
            total_topics = 0
            total_categories = 0
            for t in enriched:
                total_topics += 1
                for c in t.get('categories', []):
                    total_categories += 1
                    for n in c.get('nodes', []):
                        total_nodes += 1
                        if isinstance(n, dict) and (n.get('description') or '').strip():
                            nd_desc += 1

            print('\nContent enrichment:')
            # include elapsed if available
            try:
                print('- elapsed (s):', round(content_metrics.get('elapsed_s', 0.0), 2))
            except Exception:
                pass
            print('- topics:', total_topics, 'categories:', total_categories, 'nodes:', total_nodes, 'nodes_with_description:', nd_desc)
            try:
                if content_metrics.get('llm_usage'):
                    print('- llm_usage:', content_metrics.get('llm_usage'))
            except Exception:
                pass
        except Exception:
            pass


if __name__ == '__main__':
    main()