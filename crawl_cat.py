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
    # NOTE: removed --config flag; the positional crawl YAML defines site-specific settings
    parser.add_argument('--provider', type=str, default=None, help='LLM provider override')
    parser.add_argument('--api-token', type=str, default=None, help='LLM API token override')
    parser.add_argument('--instruction', type=str, default=None, help='LLM instruction override')
    parser.add_argument('--save-raw', action='store_true', help='Write raw extraction output with metadata to <prefix>_raw.json')
    parser.add_argument('--content', action='store_true', help='Use LLM to capture additional content (descriptions) per node')
    parser.add_argument('--approve', action='store_true', help='If selectors are proposed or provided via --review-file, write them back to the YAML')
    parser.add_argument('--review', action='store_true', help='Print proposed dom_selectors and sample deterministic extraction for review (no write). Implies --content.')
    parser.add_argument('--review-file', type=str, default=None, help='Save proposed dom selectors to this file (JSON) for offline review. Implies --content.')
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
    approve = args.approve
    review = args.review

    # Make review and review-file imply content (so the content pass and discovery run)
    if review or args.review_file:
        if not args.content:
            print('Note: --review/--review-file implies --content; enabling content pass')
        args.content = True
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

        # If dom_selectors not provided but we have an LLM, ask it to propose selectors using dom_discovery_instruction
        if not dom_selectors and dom_discovery_instruction and api_token:
            # Ask LLM to propose selectors
            try:
                _, proposed = asyncio.run(run_crawl(url, api_token, provider, dom_discovery_instruction))
                # proposed expected to be a JSON object; normalized result may be list-wrapped
                if isinstance(proposed, list) and proposed:
                    proposed = proposed[0]
                if isinstance(proposed, dict):
                    dom_proposed = proposed
                    dom_selectors = dom_proposed
            except Exception:
                dom_proposed = None

        # Run LLM extraction for content (still useful to get names->description mapping)
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
            json.dump(enriched, f, indent=2, ensure_ascii=False)

        # If the LLM proposed DOM selectors and user asked to review them, print them and samples
        if dom_proposed and review:
            try:
                print('\nProposed dom_selectors:\n')
                print(json.dumps(dom_proposed, indent=2, ensure_ascii=False))

                # show sample deterministic extraction for up to 5 nodes
                node_selectors = dom_proposed.get('node_page_selectors') if isinstance(dom_proposed, dict) else None
                if node_selectors and main_soup:
                    print('\nSample deterministic extraction using proposed node_page_selectors:\n')
                    samples = []
                    from urllib.parse import urljoin
                    for topic in normalized:
                        for c in topic.get('categories', []):
                            for n in c.get('nodes', []):
                                name = n.get('name') if isinstance(n, dict) else n
                                if not name:
                                    continue
                                # find link for this name
                                try:
                                    _, link = find_on_page_description(main_soup, name)
                                except Exception:
                                    link = None
                                if link:
                                    page_url = urljoin(url, link)
                                    sample_txt = extract_by_dom_selectors(page_url, node_selectors)
                                else:
                                    sample_txt = None
                                samples.append({'name': name, 'sample': sample_txt})
                                if len(samples) >= 5:
                                    break
                            if len(samples) >= 5:
                                break
                        if len(samples) >= 5:
                            break
                    for s in samples:
                        sample_preview = None
                        if s.get('sample'):
                            sample_preview = (s['sample'][:200] + '...') if len(s['sample']) > 200 else s['sample']
                        print(f"- {s['name']}: {sample_preview}")
            except Exception as e:
                print('Error while reviewing dom_selectors:', e)

            # optionally save proposed selectors to a file for manual inspection
            if dom_proposed and args.review_file:
                try:
                    with open(args.review_file, 'w', encoding='utf-8') as rf:
                        json.dump(dom_proposed, rf, indent=2, ensure_ascii=False)
                    print('Saved proposed dom_selectors to', args.review_file)
                except Exception as e:
                    print('Failed to save proposed dom_selectors:', e)

        # Approve and persist selectors into YAML. Support two modes:
        # - if dom_proposed exists in this run and --approve is passed, write it
        # - otherwise, if --approve and --review-file <file> provided, load selectors from file and write them
        if approve:
            try:
                # Prefer a provided review file when approving (safer and deterministic)
                selectors_to_write = None
                if args.review_file and os.path.exists(args.review_file):
                    try:
                        with open(args.review_file, 'r', encoding='utf-8') as rf:
                            selectors_to_write = json.load(rf)
                    except Exception:
                        selectors_to_write = None
                # Fallback to the in-run proposed selectors if no review file provided
                elif dom_proposed and isinstance(dom_proposed, dict):
                    selectors_to_write = dom_proposed

                # Validate selectors_to_write looks like a selector mapping
                if not selectors_to_write or not isinstance(selectors_to_write, dict):
                    print('No valid proposed selectors available to approve. Provide --review-file <file> containing the proposed selectors or run with --review and --approve together.')
                elif not any(k in selectors_to_write for k in ('index_selectors', 'node_page_selectors')):
                    print('Proposed selectors file does not look like a selector mapping (missing index_selectors/node_page_selectors). Not writing to YAML.')
                else:
                    with open(args.crawl_yaml, 'r', encoding='utf-8') as f:
                        full_cfg = yaml.safe_load(f)
                    full_cfg['dom_selectors'] = selectors_to_write
                    with open(args.crawl_yaml, 'w', encoding='utf-8') as f:
                        yaml.safe_dump(full_cfg, f)
                    print('Wrote approved dom_selectors to', args.crawl_yaml)
            except Exception as e:
                print('Failed to write dom_selectors to config:', e)

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