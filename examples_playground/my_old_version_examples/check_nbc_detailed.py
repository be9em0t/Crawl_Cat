import asyncio

async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://www.nbcnews.com/business')
        content = await page.content()
        print('Contains IE 11 text?', 'IE 11' in content or 'IE11' in content or 'Internet Explorer' in content)
        # Evaluate navigator properties
        props = await page.evaluate('''() => ({
            userAgent: navigator.userAgent,
            appVersion: navigator.appVersion,
            appName: navigator.appName,
            vendor: navigator.vendor,
            platform: navigator.platform,
            product: navigator.product,
            productSub: navigator.productSub,
            vendorSub: navigator.vendorSub,
            webdriver: navigator.webdriver
        })''')
        print('Navigator props:', props)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
