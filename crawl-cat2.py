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
print("Website: https://crawl4ai.com")


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
        merged = {"graph_nodes": [], "block_nodes": []}
        for item in all_extracted:
            if isinstance(item, dict):
                merged["graph_nodes"].extend(item.get("graph_nodes", []))
                merged["block_nodes"].extend(item.get("block_nodes", []))
            else:
                print(f"Skipping non-dict item: {type(item)} - {item}")
        save_utils.save_json(f"output/{output_file}", merged)


# Main execution
async def main(config_file, config_id=None):
    config = load_config(config_file)
    sources = config.get('sources', [])
    if not sources:
        raise ValueError("No sources found in config file")
    
    if config_id:
        source = next((s for s in sources if s.get('id') == config_id), None)
        if not source:
            available_ids = [s.get('id') for s in sources if s.get('id')]
            raise ValueError(f"Config ID '{config_id}' not found. Available IDs: {available_ids}")
    else:
        source = sources[0]  # default to first source
    url = source['url']
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
    
    # Define URLs to crawl
    base_url = "https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/"
    urls = [
        base_url + "Node-Library.html",
        base_url + "Artistic-Nodes.html",
        base_url + "Channel-Nodes.html",
        base_url + "Custom-Render-Texture-Nodes.html",
        base_url + "Input-Nodes.html",
        base_url + "Math-Nodes.html",
        base_url + "Procedural-Nodes.html",
        base_url + "ui-nodes.html",
        base_url + "Utility-Nodes.html",
        base_url + "UV-Nodes.html",
        base_url + "Block-Node.html"
    ]
    
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
    parser.add_argument('-id', '--config-id', type=str, help='ID of the source to use from the config file (defaults to first source)')
    args = parser.parse_args()
    
    asyncio.run(main(args.config, args.config_id))
