import os
import json
import yaml
import save_utils
from crawl4ai import AsyncWebCrawler, CacheMode, BrowserConfig, CrawlerRunConfig
from crawl4ai import JsonCssExtractionStrategy

async def workflow_dom(source, urls, common):
    schema = source.get('schema')
    if not schema:
        raise ValueError("Schema is required for dom workflow")

    out_folder = common.get('out_folder', '')
    output_file = source.get('out_file', 'extracted_dom')
    workflow = source.get('workflow', 'dom')
    output_file = f"{output_file}_{workflow}"
    if not output_file.endswith('.json'):
        output_file += '.json'
    if out_folder:
        output_file = f"{out_folder}/{output_file}"
    
    css_selector = source.get('css_selector')
    headless = source.get('headless', True)
    cache_mode = source.get('cache_mode', 'BYPASS')
    word_count_threshold = source.get('word_count_threshold', 1)
    page_timeout = source.get('page_timeout', 80000)
    
    main_url = source.get('url')
    if not urls:
        urls = [main_url]
    
    extraction_strategy = JsonCssExtractionStrategy(schema)
    
    config = CrawlerRunConfig(
        extraction_strategy=extraction_strategy,
        css_selector=css_selector,
        cache_mode=CacheMode[cache_mode.upper()] if cache_mode else CacheMode.BYPASS,
        word_count_threshold=word_count_threshold,
        page_timeout=page_timeout
    )
    
    async with AsyncWebCrawler() as crawler:
        if len(urls) == 1:
            result = await crawler.arun(url=urls[0], config=config)
            extracted_data = json.loads(result.extracted_content)
        else:
            # For multiple URLs, crawl each and combine
            extracted_data = []
            for url in urls:
                result = await crawler.arun(url=url, config=config)
                data = json.loads(result.extracted_content)
                extracted_data.extend(data)
    
    # Save the extracted data
    # Filter out Block nodes if present
    extracted_data = [item for item in extracted_data if item.get('category_name') != 'Block']
    save_utils.save_json(output_file, extracted_data)
    print(f"Extracted data saved to {output_file}")