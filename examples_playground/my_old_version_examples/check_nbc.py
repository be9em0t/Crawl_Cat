import asyncio

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://www.nbcnews.com/business')
        content = await page.content()
        # print small snippet
        snippet = content[:2000]
        print(snippet)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
