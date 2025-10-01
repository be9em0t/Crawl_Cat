import argparse
import asyncio
import json
import os
import base64
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def run_crawl(url, out_path, headless=True, timeout=60000):
    browser_config = BrowserConfig(headless=headless)
    crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, page_timeout=timeout)

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=crawl_config)

    # Helper to convert non-serializable objects into JSON-safe values
    def to_json_safe(obj):
        if obj is None:
            return None
        if isinstance(obj, (str, int, float, bool)):
            return obj
        if isinstance(obj, (list, tuple)):
            return [to_json_safe(x) for x in obj]
        if isinstance(obj, dict):
            return {k: to_json_safe(v) for k, v in obj.items()}
        # bytes -> base64
        if isinstance(obj, (bytes, bytearray)):
            return base64.b64encode(obj).decode('ascii')
        # pydantic/base models with dict()
        if hasattr(obj, 'dict') and callable(getattr(obj, 'dict')):
            try:
                return to_json_safe(obj.dict())
            except Exception:
                pass
        # objects with to_json()
        if hasattr(obj, 'to_json') and callable(getattr(obj, 'to_json')):
            try:
                raw = obj.to_json()
                # If it's a JSON string, parse it
                try:
                    return json.loads(raw)
                except Exception:
                    return raw
            except Exception:
                pass
        # Known markdown-like object
        if hasattr(obj, 'raw_markdown') or hasattr(obj, 'fit_markdown'):
            return {
                'raw_markdown': to_json_safe(getattr(obj, 'raw_markdown', None)),
                'fit_markdown': to_json_safe(getattr(obj, 'fit_markdown', None)),
            }
        # Fallback to str
        try:
            return str(obj)
        except Exception:
            return repr(obj)

    # Build serializable result
    serial = {
        'success': to_json_safe(getattr(result, 'success', False)),
        'status': to_json_safe(getattr(result, 'status', None)),
        'url': to_json_safe(getattr(result, 'url', url)),
        'markdown': to_json_safe(getattr(result, 'markdown', None)),
        'cleaned_html': to_json_safe(getattr(result, 'cleaned_html', None)),
        'raw_html': to_json_safe(getattr(result, 'raw_html', None)),
        'extracted_content': to_json_safe(getattr(result, 'extracted_content', None)),
        'links': to_json_safe(getattr(result, 'links', None)),
        'media': to_json_safe(getattr(result, 'media', None)),
        'screenshot': bool(getattr(result, 'screenshot', None)),
        'error': to_json_safe(getattr(result, 'error', None)),
    }

    # Ensure directory exists
    os.makedirs(os.path.dirname(out_path) or '.', exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(serial, f, indent=2, ensure_ascii=False)

    print(f'Wrote crawl result to {out_path}')


def main():
    parser = argparse.ArgumentParser(description='Run a crawl and save JSON result to a file')
    parser.add_argument('url', help='URL to crawl')
    parser.add_argument('out', help='Output JSON file path')
    parser.add_argument('--headless', action='store_true', help='Run browser headless (default false)')
    parser.add_argument('--timeout', type=int, default=60000, help='Page timeout in ms')
    args = parser.parse_args()

    # Default headless to True if flag present, otherwise False
    headless = args.headless

    asyncio.run(run_crawl(args.url, args.out, headless=headless, timeout=args.timeout))

if __name__ == '__main__':
    main()
