import asyncio

async def main():
    try:
        from playwright.async_api import async_playwright
    except Exception as e:
        print("Playwright import failed:", repr(e))
        print("If Playwright is not installed, run: pip install playwright && playwright install")
        return

    try:
        async with async_playwright() as p:
            # Prefer chromium
            if hasattr(p, "chromium"):
                print("Found Playwright and chromium is available")
                browser = await p.chromium.launch(headless=True)
                context = await browser.new_context()
                page = await context.new_page()
                # Navigate to about:blank to ensure page context
                await page.goto('about:blank')
                ua = await page.evaluate("() => navigator.userAgent")
                print("Chromium userAgent:", ua)
                await browser.close()
            else:
                print("Playwright is present but chromium is not available on this installation")
    except Exception as e:
        print("Error while launching Playwright:", repr(e))

if __name__ == '__main__':
    asyncio.run(main())
