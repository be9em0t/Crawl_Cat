import asyncio
from crawl4ai import AsyncWebCrawler
import save_utils

async def main():
    # Create an instance of AsyncWebCrawler
    async with AsyncWebCrawler() as crawler:
        # Run the crawler on a URL
        result = await crawler.arun(url="https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node-Library.html")
        # Save the extracted markdown content
        save_utils.save_data("output/simple_crawl.md", result.markdown, format="markdown")
        print("Markdown content saved to output/simple_crawl.md")

# Run the async main function
asyncio.run(main())