import re
from playwright.sync_api import Playwright, sync_playwright, expect
import os
from dotenv import load_dotenv
from datetime import date, datetime, timedelta
import time

# loads .env file into application environment
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

print(EMAIL)
print(PASSWORD)

# exit()

def run(playwright: Playwright, site, date_start, date_end) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dashboard.pirsch.io/login")
    page.get_by_role("textbox", name="Email Address").click()
    page.get_by_role("textbox", name="Email Address").fill(EMAIL)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Log In").click()
    time.sleep(2)
    page.goto(f"https://dashboard.pirsch.io/settings/import-export?domain={site}&interval=today")
    time.sleep(2)
    page.get_by_text("Settings").click()
    page.get_by_role("heading", name="Import / Export").click()
    page.get_by_role("button", name="Export Data to CSV").click()
    
    fetch_day = date_start
    while fetch_day < date_end:
        print(f"fetch day: {fetch_day}")
        formatted_date = fetch_day.strftime("%Y-%m-%d")
        page.get_by_role("textbox", name="Start Date").fill(formatted_date)
        page.get_by_role("textbox", name="End Date").fill(formatted_date)
        with page.expect_download() as download_info:
            with page.expect_popup() as page1_info:
                page.get_by_role("button", name="Create CSV File").click()
            page1 = page1_info.value
            download = download_info.value

            # Wait for the download process to complete and save the downloaded file somewhere
            download.save_as("C:/temp/" + download.suggested_filename)
            
        fetch_day += timedelta(days=1)
        time.sleep(3)
    

    
    page1.close()

    # ---------------------
    context.close()
    browser.close()    


with sync_playwright() as playwright:
    # run(playwright, "PythonFriday.dev", date(2025, 11, 7), date.today())
    run(playwright, "jgraber.ch", date(2024, 10, 1), date.today())
    # run(playwright, date(2025, 11, 6), date.today())
    # run(playwright, date(2024, 10, 1), date(2025, 10, 1))
