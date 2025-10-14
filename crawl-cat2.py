# Documentation extraction crawler that uses crawl4ai, LLM capability to analyze schema and select elements, then use DOM selectors for actual content extraction.

# Current plan is in PLAN.md

import os, sys
from dotenv import load_dotenv
load_dotenv()  # Loads from .env by default

from crawl4ai import AsyncWebCrawler, CacheMode, BrowserConfig, CrawlerRunConfig
from crawl4ai import BFSDeepCrawlStrategy, DomainFilter, FilterChain
from crawl4ai.deep_crawling.filters import URLPatternFilter, ContentRelevanceFilter
import save_utils
import llm_utils
from typing import Dict, List, Any
from pydantic import BaseModel, Field
import argparse
import json
import yaml
import asyncio
import re

print("Crawl4AI: Advanced Web Crawling and Data Extraction")
print("GitHub Repository: https://github.com/unclecode/crawl4ai")
print("Twitter: @unclecode")
print("Website: https://crawl4ai.com \n")


def parse_markdown_table(content: str) -> List[Dict[str, str]]:
    """Parse markdown table to extract links and descriptions."""
    lines = content.split('\n')
    table_start = False
    headers = []
    rows = []

    for line in lines:
        line = line.strip()
        if '**Topic**' in line and '**Description**' in line:
            table_start = True
            headers = ['topic', 'description']
            continue
        elif table_start and '---' in line:
            continue
        elif table_start and '|' in line and not line.startswith('##'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 2:
                topic = parts[0]
                description = parts[1] if len(parts) > 1 else ""
                # Extract link from [text](url)
                link_match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', topic)
                if link_match:
                    name = link_match.group(1)
                    url = link_match.group(2)
                    rows.append({
                        'name': name,
                        'url': url,
                        'description': description
                    })
        elif table_start and line.startswith('##'):
            # New section, stop parsing table
            break

    return rows


def build_hierarchy(flat_data: List[Dict[str, Any]], root_url: str) -> Dict[str, Any]:
    """Build hierarchical structure from flat crawled data."""
    # Create lookup by URL, normalize
    url_to_content = {}
    for item in flat_data:
        url = item['url'].replace('%40', '@')
        url_to_content[url] = item['content']

    if root_url not in url_to_content:
        raise ValueError("Root URL not found in data")

    root_content = url_to_content[root_url]

    # Parse root for categories
    categories = parse_markdown_table(root_content)

    hierarchy = {
        'name': 'Node Library',
        'url': root_url,
        'description': 'Explore nodes that enable color and channel manipulation...',
        'categories': []
    }

    for cat in categories:
        cat_url = cat['url']
        if cat_url in url_to_content:
            cat_content = url_to_content[cat_url]
            # Parse category for subcategories and nodes
            sub_sections = parse_category_content(cat_content)
            hierarchy['categories'].append({
                'name': cat['name'],
                'url': cat_url,
                'description': cat['description'],
                'subcategories': sub_sections
            })

    return hierarchy


def parse_category_content(content: str) -> List[Dict[str, Any]]:
    """Parse category page content for subcategories and nodes."""
    lines = content.split('\n')
    subcategories = []
    current_sub = None

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('## ') and '[](' in line:
            # New subcategory
            sub_match = re.search(r'##\s+\[\]\(([^)]+)#([^)]+)\)(.+)', line)
            if sub_match:
                anchor = sub_match.group(2)
                title = sub_match.group(3).strip()
                current_sub = {
                    'name': title,
                    'anchor': anchor,
                    'nodes': []
                }
                subcategories.append(current_sub)
                # Look for table after this
                i += 1
                while i < len(lines):
                    table_line = lines[i].strip()
                    if '**Topic**' in table_line and '**Description**' in table_line:
                        # Parse table
                        table_content = []
                        i += 1  # skip the header line
                        if i < len(lines) and '---' in lines[i].strip():
                            i += 1  # skip the separator line
                        while i < len(lines) and not lines[i].strip().startswith('##'):
                            table_content.append(lines[i])
                            i += 1
                        table_str = '**Topic** | **Description**\n---|---\n' + '\n'.join(table_content)
                        nodes = parse_markdown_table(table_str)
                        if current_sub:
                            current_sub['nodes'] = nodes
                        break
                    i += 1
            else:
                print("Regex did not match")
                i += 1
        elif '**Topic**' in line and '**Description**' in line and not current_sub:
            # Direct nodes without subcategory
            table_content = []
            i += 1
            if i < len(lines) and '---' in lines[i].strip():
                i += 1
            while i < len(lines) and not lines[i].strip().startswith('##'):
                table_content.append(lines[i])
                i += 1
            table_str = '**Topic** | **Description**\n---|---\n' + '\n'.join(table_content)
            nodes = parse_markdown_table(table_str)
            if nodes:
                subcategories.append({
                    'name': 'General',
                    'nodes': nodes
                })
        else:
            i += 1

    return subcategories


# LLM Extraction Example
# class OpenAIModelFee(BaseModel):
#     model_name: str = Field(..., description="Name of the OpenAI model.")
#     input_fee: str = Field(..., description="Fee for input token for the OpenAI model.")
#     output_fee: str = Field(..., description="Fee for output token for the OpenAI model.")


def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


async def workflow_llm(source, urls):
    llm_alias = source['llm']
    provider, env_var = llm_utils.get_provider_info(llm_alias)
    api_token = os.getenv(env_var) if env_var else None
    
    instruction = source.get('instruction', '')
    schema_model = None
    if 'pydantic_model' in source and source['pydantic_model']:
        exec(source['pydantic_model'], globals())
        # Find the main class (assume NodeLibrary)
        main_class = 'NodeLibrary'
        if main_class in globals():
            schema_model = globals()[main_class]
        else:
            # Find any class
            for name in globals():
                if isinstance(globals()[name], type) and issubclass(globals()[name], BaseModel):
                    schema_model = globals()[name]
                    break
            else:
                raise ValueError("No Pydantic model class found in generated code")
    
    extraction_type = source.get('extraction_type', 'schema')
    extra_args = {
        "temperature": source.get('temperature', 0),
        "top_p": source.get('top_p', 0.9),
        "max_tokens": source.get('max_tokens', 2000)
    }
    output_file = source.get('out_file', 'extracted')
    if not output_file.endswith('.json'):
        output_file += '.json'
    css_selector = source.get('css_selector')
    headless = source.get('headless', True)
    cache_mode = source.get('cache_mode', 'BYPASS')
    word_count_threshold = source.get('word_count_threshold', 1)
    page_timeout = source.get('page_timeout', 80000)
    
    await llm_utils.extract_structured_data_using_llm(
        provider=provider,
        api_token=api_token,
        urls=urls,
        instruction=instruction,
        schema_model=schema_model,
        extra_args=extra_args,
        headless=headless,
        cache_mode=cache_mode,
        word_count_threshold=word_count_threshold,
        page_timeout=page_timeout,
        output_file=output_file,
        css_selector=css_selector,
        extraction_type=extraction_type
    )


async def workflow_explore(source, urls):
    from urllib.parse import urlparse
    
    class BlockedURLFilter:
        def __init__(self, blocked_patterns):
            self.blocked_patterns = blocked_patterns
        
        def filter(self, url):
            from fnmatch import fnmatch
            for pattern in self.blocked_patterns:
                if fnmatch(url, pattern):
                    return False
            return True
        
        def apply(self, url):
            return self.filter(url)
    
    llm_alias = source['llm']  # Not used, but keep for consistency
    headless = source.get('headless', True)
    cache_mode = source.get('cache_mode', 'BYPASS')
    word_count_threshold = source.get('word_count_threshold', 1)
    page_timeout = source.get('page_timeout', 80000)
    out_file = source.get('out_file', 'explore_output')
    out_formats = source.get('out_format', ['json'])
    if isinstance(out_formats, str):
        out_formats = [out_formats]
    css_selector = source.get('css_selector', None)
    deep_crawl = source.get('deep_crawl', False)
    max_depth = source.get('max_depth', 3)
    max_pages = source.get('max_pages', 10)
    
    # For explore, we expect only one URL (the main page)
    if len(urls) != 1:
        print(f"Warning: Explore workflow expects 1 URL, got {len(urls)}. Using first URL.")
    url = urls[0]
    
    print(f"\n--- Exploring structure from {url} ---")
    
    browser_config = BrowserConfig(headless=headless)
    
    cache_mode_enum = getattr(CacheMode, cache_mode.upper(), CacheMode.BYPASS)
    
    if deep_crawl:
        # Build filter chain from config
        filters = source.get('filters', [])
        filter_instances = []
        for f in filters:
            f_type = f['type']
            if f_type == 'DomainFilter':
                filter_instances.append(DomainFilter(**{k: v for k, v in f.items() if k != 'type'}))
            elif f_type == 'URLPatternFilter':
                allowed = f.get('patterns', [])
                blocked = f.get('blocked_patterns', [])
                if allowed:
                    filter_instances.append(URLPatternFilter(patterns=allowed))
                if blocked:
                    filter_instances.append(BlockedURLFilter(blocked))
            elif f_type == 'ContentRelevanceFilter':
                filter_instances.append(ContentRelevanceFilter(**{k: v for k, v in f.items() if k != 'type'}))
            else:
                print(f"Warning: Unknown filter type '{f_type}', skipping.")
        
        # Default to domain filter if no filters specified
        if not filter_instances:
            domain = urlparse(url).netloc
            filter_instances = [DomainFilter(allowed_domains=[domain])]
        
        filter_chain = FilterChain(filter_instances)
        deep_crawl_strategy = BFSDeepCrawlStrategy(
            max_depth=max_depth,
            max_pages=max_pages,
            filter_chain=filter_chain
        )
        crawler_config = CrawlerRunConfig(
            cache_mode=cache_mode_enum,
            word_count_threshold=word_count_threshold,
            page_timeout=page_timeout,
            css_selector=css_selector,
            verbose=True,
            deep_crawl_strategy=deep_crawl_strategy
        )
    else:
        crawler_config = CrawlerRunConfig(
            cache_mode=cache_mode_enum,
            word_count_threshold=word_count_threshold,
            page_timeout=page_timeout,
            css_selector=css_selector,
            verbose=True,
        )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun(url=url, config=crawler_config)
    
    # Handle results: single page or list
    if not isinstance(results, list):
        results = [results]
    
    print(f"Explored {len(results)} pages")
    
    for fmt in out_formats:
        if fmt == 'markdown':
            combined_content = ""
            for i, result in enumerate(results):
                combined_content += f"\n--- Page {i+1}: {result.url} ---\n\n"
                combined_content += result.markdown.raw_markdown + "\n"
            file_ext = ".md"
            save_utils.save_data(f"output/{out_file}{file_ext}", combined_content, 'markdown')
        elif fmt == 'json':
            pages_data = [{"url": result.url, "content": result.markdown.raw_markdown} for result in results]
            file_ext = ".json"
            save_utils.save_json(f"output/{out_file}{file_ext}", pages_data)
        print(f"Saved {fmt} output to output/{out_file}{file_ext}")


async def workflow_pydantic(source, urls):
    out_file = source.get('out_file', 'pydantic_output')
    explore_md_path = f"output/{out_file}.md"
    explore_json_path = f"output/{out_file}.json"
    
    if not os.path.exists(explore_md_path) or not os.path.exists(explore_json_path):
        raise ValueError(f"Explore outputs not found: {explore_md_path} and {explore_json_path}. Run explore workflow first with out_file: '{out_file}'.")
    
    with open(explore_md_path, 'r') as f:
        explore_md = f.read()
    
    with open(explore_json_path, 'r') as f:
        explore_json = json.load(f)
    
    # Get the prompt from config
    base_prompt = source.get('prompt', '')
    
    # Build the full prompt including the data
    prompt = base_prompt + f"\n\nExplore Markdown (truncated if necessary):\n{explore_md[:10000]}...\n\nExplore JSON (first 5 pages):\n{json.dumps(explore_json[:5], indent=2)}"
    
    llm_alias = source['llm']
    temperature = source.get('temperature', 0.0)
    top_p = source.get('top_p', 0.9)
    max_tokens = source.get('max_tokens', 8000)
    
    provider, env_var = llm_utils.get_provider_info(llm_alias)
    api_token = os.getenv(env_var) if env_var else None
    
    if api_token is None and not provider.startswith("ollama"):
        print(f"API token is required for {provider}. Skipping.")
        return
    
    extra_args = {
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens
    }
    
    # Call LLM directly with the prompt
    model_code = await llm_utils.call_llm_directly(provider, api_token, prompt, extra_args)
    
    # Clean the model_code by removing markdown code blocks
    if model_code.startswith('```python'):
        model_code = model_code[9:]
    if model_code.endswith('```'):
        model_code = model_code[:-3]
    model_code = model_code.strip()
    
    # Save the model code
    model_file = f"output/{out_file}_model.py"
    with open(model_file, 'w') as f:
        f.write(model_code)
    print(f"Saved Pydantic models to {model_file}")
    
    # Execute the model code to get the classes
    try:
        exec(model_code, globals())
        # Find the main class (assume NodeLibrary)
        main_class = 'NodeLibrary'
        if main_class in globals():
            ModelClass = globals()[main_class]
        else:
            # Find any class
            for name in globals():
                if isinstance(globals()[name], type) and issubclass(globals()[name], BaseModel):
                    ModelClass = globals()[name]
                    break
            else:
                raise ValueError("No Pydantic model class found in generated code")
        
        print(f"Using model class: {ModelClass.__name__}")
        
        # Now, use the model for extraction
        await extract_structured_data_using_llm(
            provider=provider, 
            api_token=api_token, 
            urls=urls, 
            instruction=source.get('instruction', ''), 
            schema_model=ModelClass, 
            extra_args=extra_args,
            headless=source.get('headless', True),
            cache_mode=source.get('cache_mode', 'BYPASS'),
            word_count_threshold=source.get('word_count_threshold', 1),
            page_timeout=source.get('page_timeout', 80000),
            output_file=f"{out_file}_pydantic.json",
            css_selector=source.get('css_selector'),
            extraction_type="schema"
        )
        
    except Exception as e:
        print(f"Error processing generated model or extracting: {e}")
        # Save empty structured JSON
        save_utils.save_json(f"output/{out_file}_pydantic.json", {})


async def workflow_hierarchy(source, urls):
    input_file = source.get('input_file')
    if not input_file:
        raise ValueError("input_file required for hierarchy workflow")
    
    explore_json_path = f"output/{input_file}"
    
    if not os.path.exists(explore_json_path):
        raise ValueError(f"Explore JSON not found: {explore_json_path}. Run explore workflow first.")
    
    with open(explore_json_path, 'r') as f:
        flat_data = json.load(f)
    
    root_url = source.get('url')
    if not root_url:
        raise ValueError("url required for hierarchy workflow")
    
    # Build hierarchy
    hierarchy = build_hierarchy(flat_data, root_url)
    
    # Save
    out_file = source.get('out_file', 'hierarchy_output')
    hierarchy_file = f"output/{out_file}.json"
    with open(hierarchy_file, 'w') as f:
        json.dump(hierarchy, f, indent=2)
    
    print(f"Hierarchical JSON saved to {hierarchy_file}")


# Main execution
async def main(config_file, config_id=None):
    config = load_config(config_file)
    sources = config.get('sources', [])
    if not sources:
        raise ValueError("No sources found in config file")
    
    if not config_id:
        available_ids = [s.get('id') for s in sources if s.get('id')]
        raise ValueError(f"Config ID is required. Available IDs: {available_ids}")
    
    source = next((s for s in sources if s.get('id') == config_id), None)
    if not source:
        available_ids = [s.get('id') for s in sources if s.get('id')]
        raise ValueError(f"Config ID '{config_id}' not found. \nAvailable IDs: {available_ids}")
    
    if 'workflow' not in source:
        raise ValueError("Workflow key missing")
    
    workflow = source['workflow']
    allowed_workflows = ['llm', 'explore', 'pydantic', 'hierarchy']
    if workflow not in allowed_workflows:
        raise ValueError("Workflow key invalid")
    
    # Only get URLs for workflows that need them
    urls = None
    if workflow in ['llm', 'explore', 'pydantic']:
        urls = source.get('urls') or [source['url']]
    
    if workflow == 'llm':
        await workflow_llm(source, urls)
    elif workflow == 'explore':
        await workflow_explore(source, urls)
    elif workflow == 'pydantic':
        await workflow_pydantic(source, urls)
    elif workflow == 'hierarchy':
        await workflow_hierarchy(source, urls)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Crawl and extract structured data using LLM",
        epilog="""
Usage examples:
  python crawl-cat2.py -cfg config_openai_fees.yaml
  python crawl-cat2.py -cfg config_openai_fees.yaml -id openai_fees_or-gpt4o-mini

Required files:
- guidance_fees_gpt.yaml: Configuration file with sources, URLs, models, etc.
- providers.yaml: Provider definitions with LLM aliases and API keys
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-cfg', '--config', type=str, required=True, help='Path to the configuration YAML file')
    parser.add_argument('-id', '--config-id', type=str, help='ID of the source to use from the config file')
    args = parser.parse_args()
    
    try:
        asyncio.run(main(args.config, args.config_id))
    except ValueError as e:
        print(f"Configuration Error: {e}")
        sys.exit(1)
