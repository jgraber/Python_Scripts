import time
from playwright.sync_api import Playwright, sync_playwright, expect

urls = []

def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    print(f"Total Urls to check: {len(urls)}")

    page = context.new_page()

    for url in urls:
        page.goto(url)

        title = page.title();
        print(title)

        copyright = page.get_by_role("link", name="GeneratePress")
        copyright.scroll_into_view_if_needed()
        
        time.sleep(2)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    with open("pages.txt", "r") as x:
        while True:
            line = x.readline()
            if not line:
                break
            urls.append(line)
        
    run(playwright)
