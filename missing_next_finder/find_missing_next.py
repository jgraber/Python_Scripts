import requests
from bs4 import BeautifulSoup
import re

def has_next_header(content : BeautifulSoup) -> bool:
    headings = content.find_all("h2")
    for head in headings:
        # print(head)
        if head.text == "Next":
            return True
    return False

def search_links(content : BeautifulSoup, page: str):
    m = re.search(r'<h2>Next</h2>.*?<h3', page, re.DOTALL)
    s = m.start()
    e = m.end() - len('<h3')
    target_html = page[s:e]
    # print(target_html)
    new_bs = BeautifulSoup(target_html, 'html.parser')
    links = new_bs.find_all("a", href=True)
    for link in links:
        print(f"\t - {link}")
    if len(links) == 0:
        print("*** No links found ***")
    # print(new_bs.prettify())

def fetch_content(url : str) -> str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    print(f"\n\n{soup.title.text}")
    if has_next_header(soup):
        print(f"found a next section in {url.strip()}")
        search_links(soup, page.text)
    else:
        print(f"No Next section in {url}")

# fetch_content("https://jgraber.ch/index.php")
        
if __name__ == "__main__":
    urls = []

    with open("pages_cleaned.txt", "r") as x:
        while True:
            line = x.readline()
            if not line:
                break
            urls.append(line)
    
    print(f"Total Urls to check: {len(urls)}")

    for url in urls:
        try:
            fetch_content(url)
        except Exception as error:
            print(f"{url} throws {error}")
    # fetch_content("https://improveandrepeat.com/2024/03/python-friday-220-manage-to-dos-with-fastapi/")