import click 
from datetime import date, datetime, timedelta
from requests import options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import logging
import os
from dotenv import load_dotenv
import time

def prepare_browser():
    load_dotenv()
    logging.getLogger('WDM').setLevel(logging.NOTSET)
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.implicitly_wait(2)

    driver.get(os.getenv('login_page'))
    username = driver.find_element(by=By.ID, value="usernameOrEmail")
    username.send_keys(os.getenv('user'))
    cont = driver.find_element(by=By.CLASS_NAME, value="form-button")
    cont.click()
    password = driver.find_element(by=By.ID, value="password")
    password.send_keys(os.getenv('password'))
    submit = driver.find_element(by=By.CLASS_NAME, value="form-button")
    submit.click()
    time.sleep(5)
    return driver

def fetch_stats(folder, date_start, date_end):
    date_start = min(date_start, date.today())
    date_end = min(date_end, date.today())

    print(f"folder: {folder}")
    print(f"start: {date_start}")
    print(f"end: {date_end}")

    driver = prepare_browser()

    fetch_day = date_start
    while fetch_day < date_end:
        print(f"fetch day: {fetch_day}")
        # do work
        fetch_stats_for_day(folder, fetch_day, driver)
        fetch_day += timedelta(days=1)

    print("wait to finish downloads...")
    time.sleep(10)
    driver.quit()


def fetch_stats_for_day(folder, day, driver):
    print(f"work on {day}")
    # posts = f"https://wordpress.com/stats/day/posts/improveandrepeat.com?startDate={day}"
    # driver.get(posts)
    # countries = f"https://wordpress.com/stats/day/countryviews/improveandrepeat.com?startDate={day}"
    # driver.get(countries)
    # referer = f"https://wordpress.com/stats/day/searchterms/improveandrepeat.com?startDate={day}"
    # driver.get(referer)
    clicks = f"https://wordpress.com/stats/day/clicks/improveandrepeat.com?startDate={day}"
    driver.get(clicks)
    time.sleep(2)
    # driver.execute_script("document.getElementByClassName('jetpack-colophon').scrollIntoView();")
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    download = driver.find_element(by=By.CLASS_NAME, value="stats-download-csv")
    download.click()



# https://www.markhneedham.com/blog/2019/07/29/python-click-date-parameter-type/
@click.command()
@click.option('--date-start', type=click.DateTime(formats=["%Y-%m-%d"]),
              default=str(date.today()))
@click.option('--date-end', type=click.DateTime(formats=["%Y-%m-%d"]),
              default=str(date.today()))
@click.argument('folder', type=click.Path(exists=True))
@click.version_option(version='1.0.0')
def fetch(folder, date_start, date_end):
    """Splits the files inside a folder into subfolders (by date or month)"""
    fetch_stats(folder, date_start.date(), date_end.date())


if __name__ == '__main__':
    fetch()