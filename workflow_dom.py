import os
import json
import yaml
import save_utils
from crawl4ai import AsyncWebCrawler, CacheMode, BrowserConfig, CrawlerRunConfig
from crawl4ai import JsonCssExtractionStrategy

async def workflow_dom(source, urls, common):
    category_schema = source.get('category_schema') or source.get('schema')
    if not category_schema:
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
    
    extraction_strategy = JsonCssExtractionStrategy(category_schema)
    
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
            categories = json.loads(result.extracted_content)
        else:
            # For multiple URLs, combine
            categories = []
            for url in urls:
                result = await crawler.arun(url=url, config=config)
                data = json.loads(result.extracted_content)
                categories.extend(data)
    
    # Filter categories if needed
    categories = [item for item in categories if item.get('category_name') != 'Block']
    
    expand_nodes = source.get('expand_nodes', False)
    if expand_nodes:
        preview_limit = source.get('preview_limit')
        processed_nodes = 0
        node_schema = source.get('node_schema')
        node_detail_schema = source.get('node_detail_schema')
        
        node_config = CrawlerRunConfig(
            extraction_strategy=JsonCssExtractionStrategy(node_schema),
            css_selector=css_selector,
            cache_mode=CacheMode[cache_mode.upper()] if cache_mode else CacheMode.BYPASS,
            word_count_threshold=word_count_threshold,
            page_timeout=page_timeout
        )
        
        detail_config = CrawlerRunConfig(
            extraction_strategy=JsonCssExtractionStrategy(node_detail_schema),
            css_selector=None,  # Whole page
            cache_mode=CacheMode[cache_mode.upper()] if cache_mode else CacheMode.BYPASS,
            word_count_threshold=word_count_threshold,
            page_timeout=page_timeout
        )
        
        for cat in categories:
            cat_url = cat.get('category_url')
            if cat_url:
                # Make full URL if relative
                if not cat_url.startswith('http'):
                    from urllib.parse import urljoin
                    cat_url = urljoin(main_url, cat_url)
                
                async with AsyncWebCrawler() as node_crawler:
                    result = await node_crawler.arun(url=cat_url, config=node_config)
                    save_utils.save_text("debug_artistic.html", result.cleaned_html)
                    nodes = json.loads(result.extracted_content)
                
                # For each node, get details
                for node in nodes:
                    if preview_limit and processed_nodes >= preview_limit:
                        break
                    node_url = node.get('node_url')
                    if node_url:
                        if not node_url.startswith('http'):
                            node_url = urljoin(cat_url, node_url)
                        node['node_url'] = node_url  # Update to full URL
                        
                        async with AsyncWebCrawler() as detail_crawler:
                            result = await detail_crawler.arun(url=node_url, config=detail_config)
                            details = json.loads(result.extracted_content)
                            if details:
                                node.update(details[0])  # Assuming one item
                    processed_nodes += 1
                
                cat['nodes'] = nodes
            if preview_limit and processed_nodes >= preview_limit:
                break
    
    # Save the extracted data
    save_utils.save_json(output_file, categories)
    print(f"Extracted data saved to {output_file}")