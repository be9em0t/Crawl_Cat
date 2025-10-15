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

from workflow_llm import workflow_llm
from workflow_explore import workflow_explore
from workflow_pydantic import workflow_pydantic
from workflow_hierarchy import workflow_hierarchy

print("Crawl4AI: Advanced Web Crawling and Data Extraction")
print("GitHub Repository: https://github.com/unclecode/crawl4ai")
print("Twitter: @unclecode")
print("Website: https://crawl4ai.com \n")


def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


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
