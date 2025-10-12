import os, sys
from dotenv import load_dotenv
load_dotenv()  # Loads from .env by default

from crawl4ai import LLMConfig

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

import asyncio
import json
import yaml
import argparse
from typing import Dict, List
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, CacheMode, BrowserConfig, CrawlerRunConfig
from crawl4ai import LLMExtractionStrategy
import save_utils

print("Crawl4AI: Advanced Web Crawling and Data Extraction")
print("GitHub Repository: https://github.com/unclecode/crawl4ai")
print("Twitter: @unclecode")
print("Website: https://crawl4ai.com \n")


# LLM Extraction Example
# class OpenAIModelFee(BaseModel):
#     model_name: str = Field(..., description="Name of the OpenAI model.")
#     input_fee: str = Field(..., description="Fee for input token for the OpenAI model.")
#     output_fee: str = Field(..., description="Fee for output token for the OpenAI model.")


def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def get_provider_info(llm_alias, providers_file='providers.yaml'):
    providers = load_config(providers_file)['providers']
    for key, info in providers.items():
        if llm_alias in info.get('aliases', []) or key == llm_alias:
            return info['provider'], info['env_var']
    raise ValueError(f"LLM alias '{llm_alias}' not found in providers.yaml")


def create_dynamic_model(model_str):
    if model_str.strip().startswith('from'):
        # Model string defines classes, exec it and return the last defined class
        exec(model_str, globals())
        lines = model_str.strip().split('\n')
        for line in reversed(lines):
            if line.strip().startswith('class '):
                class_name = line.split()[1].split('(')[0]
                return globals()[class_name]
    else:
        # Original logic for simple field definitions
        indented_model_str = '\n'.join('    ' + line for line in model_str.split('\n') if line.strip())
        model_code = f"""
class DynamicModel(BaseModel):
{indented_model_str}
"""
        exec(model_code, globals())
        return DynamicModel


async def extract_structured_data_using_llm(
    provider: str, api_token: str = None, urls: List[str] = None, instruction: str = None, schema_model = None, extra_args: Dict[str, any] = None,
    headless: bool = True, cache_mode: str = "BYPASS", word_count_threshold: int = 1, page_timeout: int = 80000, output_file: str = "extracted_fees.json", css_selector: str = None, extraction_type: str = "schema"
):
    print(f"\n--- Extracting Structured Data with {provider} ---")

    if api_token is None and not provider.startswith("ollama"):
        print(f"API token is required for {provider}. Skipping this example.")
        return

    browser_config = BrowserConfig(headless=headless)

    if extra_args is None:
        extra_args = {"temperature": 0, "top_p": 0.9, "max_tokens": 2000}

    cache_mode_enum = getattr(CacheMode, cache_mode.upper(), CacheMode.BYPASS)

    all_extracted = []

    for url in urls:
        print(f"Processing {url}")
        crawler_config = CrawlerRunConfig(
            cache_mode=cache_mode_enum,
            word_count_threshold=word_count_threshold,
            page_timeout=page_timeout,
            css_selector=css_selector,
            verbose=True,
            extraction_strategy=LLMExtractionStrategy(
                llm_config=LLMConfig(provider=provider,api_token=api_token),
                schema=schema_model.model_json_schema() if extraction_type == "schema" else None,
                extraction_type=extraction_type,
                instruction=instruction,
                extra_args=extra_args,
            ),
        )

        async with AsyncWebCrawler(config=browser_config) as crawler:
            result = await crawler.arun(
                url=url, config=crawler_config
            )
            print(f"Extracted from {url}: {len(result.extracted_content)} items")
            extracted = json.loads(result.extracted_content)
            if isinstance(extracted, list):
                all_extracted.extend(extracted)
            else:
                all_extracted.append(extracted)

    print(f"Total extracted: {len(all_extracted)} items")
    if extraction_type == "block":
        save_utils.save_json(f"output/{output_file}", all_extracted)
    else:
        merged_graph = {}
        merged_block = {}
        
        def merge_categories(target, source):
            for cat in source:
                name = cat['name']
                if name not in target:
                    target[name] = {'name': name, 'subcategories': {}, 'nodes': []}
                if cat.get('subcategories'):
                    for sub in cat['subcategories'] or []:
                        sub_name = sub['name']
                        if sub_name not in target[name]['subcategories']:
                            target[name]['subcategories'][sub_name] = {'name': sub_name, 'nodes': []}
                        target[name]['subcategories'][sub_name]['nodes'].extend(sub.get('nodes', []))
                        # Deduplicate nodes
                        nodes_dict = {node['name']: node for node in target[name]['subcategories'][sub_name]['nodes']}
                        target[name]['subcategories'][sub_name]['nodes'] = list(nodes_dict.values())
                if cat.get('nodes'):
                    target[name]['nodes'].extend(cat['nodes'])
                    # Deduplicate nodes
                    nodes_dict = {node['name']: node for node in target[name]['nodes']}
                    target[name]['nodes'] = list(nodes_dict.values())
        
        for item in all_extracted:
            if isinstance(item, dict):
                merge_categories(merged_graph, item.get("graph_nodes", []))
                merge_categories(merged_block, item.get("block_nodes", []))
        
        # Convert back to list
        final_graph = []
        for cat_name, cat_data in merged_graph.items():
            subcats = []
            for sub_name, sub_data in cat_data['subcategories'].items():
                subcats.append({'name': sub_name, 'nodes': sub_data['nodes']})
            final_graph.append({
                'name': cat_name,
                'subcategories': subcats if subcats else None,
                'nodes': cat_data['nodes'] if cat_data['nodes'] else None
            })
        
        final_block = []
        for cat_name, cat_data in merged_block.items():
            subcats = []
            for sub_name, sub_data in cat_data['subcategories'].items():
                subcats.append({'name': sub_name, 'nodes': sub_data['nodes']})
            final_block.append({
                'name': cat_name,
                'subcategories': subcats if subcats else None,
                'nodes': cat_data['nodes'] if cat_data['nodes'] else None
            })
        
async def workflow_explore(source, urls):
    from urllib.parse import urlparse
    
    llm_alias = source['llm']  # Not used, but keep for consistency
    headless = source.get('headless', True)
    cache_mode = source.get('cache_mode', 'BYPASS')
    word_count_threshold = source.get('word_count_threshold', 1)
    page_timeout = source.get('page_timeout', 80000)
    out_file = source.get('out_file', 'explore_output')
    out_format = source.get('out_format', 'json')
    output_file = f"{out_file}.md" if out_format == 'markdown' else f"{out_file}.json"
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
        from crawl4ai import BFSDeepCrawlStrategy, DomainFilter, FilterChain
        domain = urlparse(url).netloc
        filter_chain = FilterChain([DomainFilter(allowed_domains=[domain])])
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
    
    if out_format == 'markdown':
        # Concatenate all markdowns with separators
        combined_content = ""
        for i, result in enumerate(results):
            combined_content += f"\n--- Page {i+1}: {result.url} ---\n\n"
            combined_content += result.markdown.raw_markdown + "\n"
        save_utils.save_data(f"output/{output_file}", combined_content, 'markdown')
    else:
        # Save as JSON list
        pages_data = [{"url": result.url, "content": result.markdown.raw_markdown} for result in results]
        save_utils.save_json(f"output/{output_file}", pages_data)
    
    print(f"Saved explore output to output/{output_file}")


async def workflow_llm(source, urls):
    instruction = source['instruction']
    pydantic_model_str = source['pydantic_model']
    llm_alias = source['llm']
    temperature = source.get('temperature', 0.0)
    top_p = source.get('top_p', 0.9)
    max_tokens = source.get('max_tokens', 4000)
    headless = source.get('headless', True)
    cache_mode = source.get('cache_mode', 'BYPASS')
    word_count_threshold = source.get('word_count_threshold', 1)
    page_timeout = source.get('page_timeout', 80000)
    out_file = source.get('out_file', 'extracted_fees')
    output_file = f"{out_file}.json"
    css_selector = source.get('css_selector', None)
    extraction_type = source.get('extraction_type', 'schema')
    
    provider, env_var = get_provider_info(llm_alias)
    api_token = os.getenv(env_var) if env_var else None
    
    schema_model = create_dynamic_model(pydantic_model_str)
    
    extra_args = {
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens
    }
    
    await extract_structured_data_using_llm(
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
    allowed_workflows = ['llm', 'explore']
    if workflow not in allowed_workflows:
        raise ValueError("Workflow key invalid")
    
    urls = source.get('urls') or [source['url']]
    
    if workflow == 'llm':
        await workflow_llm(source, urls)
    elif workflow == 'explore':
        await workflow_explore(source, urls)


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
