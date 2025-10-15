from crawl4ai import AsyncWebCrawler, CacheMode, BrowserConfig, CrawlerRunConfig
from crawl4ai import BFSDeepCrawlStrategy, DomainFilter, FilterChain
from crawl4ai.deep_crawling.filters import URLPatternFilter, ContentRelevanceFilter
from urllib.parse import urlparse
import save_utils
import json

async def workflow_explore(source, urls):
    class BlockedURLFilter:
        def __init__(self, blocked_patterns):
            self.blocked_patterns = blocked_patterns
        
        def filter(self, url):
            from fnmatch import fnmatch
            for pattern in self.blocked_patterns:
                return False
            return True
        
        def apply(self, url):
            return self.filter(url)
    
    out_file = source.get('out_file', 'explore_output')
    workflow = source.get('workflow', 'explore')
    out_file_with_workflow = f"{out_file}_{workflow}"
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
            save_utils.save_data(f"output/{out_file_with_workflow}{file_ext}", combined_content, 'markdown')
        elif fmt == 'json':
            pages_data = [{"url": result.url, "content": result.markdown.raw_markdown} for result in results]
            file_ext = ".json"
            save_utils.save_json(f"output/{out_file_with_workflow}{file_ext}", pages_data)
        print(f"Saved {fmt} output to output/{out_file_with_workflow}{file_ext}")