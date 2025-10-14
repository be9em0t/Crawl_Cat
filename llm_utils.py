import os
from dotenv import load_dotenv
load_dotenv()  # Loads from .env by default

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

try:
    import ollama
except ImportError:
    ollama = None

from crawl4ai import LLMConfig
import json
import yaml
from typing import Dict, List, Any
import save_utils


def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def get_provider_info(llm_alias, providers_file='providers.yaml'):
    providers = load_config(providers_file)['providers']
    for key, info in providers.items():
        if llm_alias in info.get('aliases', []) or key == llm_alias:
            return info['provider'], info['env_var']
    raise ValueError(f"LLM alias '{llm_alias}' not found in providers.yaml")


async def call_llm_directly(provider, api_token, prompt, extra_args):
    """Call LLM directly without crawling."""
    if provider.startswith("openai") or provider.startswith("openrouter"):
        if OpenAI is None:
            raise ImportError("OpenAI library not installed. Install with: pip install openai")
        base_url = "https://openai.com/v1" if provider.startswith("openai") else "https://openrouter.ai/api/v1"
        client = OpenAI(api_key=api_token, base_url=base_url)
        model = provider.split("/")[-1] if "/" in provider else provider
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            **extra_args
        )
        return response.choices[0].message.content.strip()
    elif provider.startswith("ollama"):
        if ollama is None:
            raise ImportError("Ollama library not installed. Install with: pip install ollama")
        model = provider.split("/")[-1]
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            options=extra_args
        )
        return response['message']['content'].strip()
    else:
        raise ValueError(f"Unsupported provider: {provider}")


async def extract_structured_data_using_llm(
    provider: str, api_token: str = None, urls: List[str] = None, instruction: str = None, schema_model = None, extra_args: Dict[str, any] = None,
    headless: bool = True, cache_mode: str = "BYPASS", word_count_threshold: int = 1, page_timeout: int = 80000, output_file: str = "extracted_fees.json", css_selector: str = None, extraction_type: str = "schema"
):
    print(f"\n--- Extracting Structured Data with {provider} ---")

    if api_token is None and not provider.startswith("ollama"):
        print(f"API token is required for {provider}. Skipping this example.")
        return

    from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
    from crawl4ai import LLMExtractionStrategy

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
                schema=schema_model.model_json_schema() if extraction_type == "schema" and schema_model else None,
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
                merge_categories(merged_graph, item.get("graph_nodes") or [])
                merge_categories(merged_block, item.get("block_nodes") or [])
        
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
        
        save_utils.save_json(f"output/{output_file}", {"graph_nodes": final_graph, "block_nodes": final_block})