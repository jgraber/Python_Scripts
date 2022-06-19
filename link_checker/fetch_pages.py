# pip install beautifulsoup4 requests
from bs4 import BeautifulSoup 
import requests

all_links = []

def process_link(line):
    content = requests.get(line)
    soup = BeautifulSoup(content.text, 'html.parser')
    links = soup.find_all("a")
    for link in links:
        link_text = link.get_text().strip()
        link_text_clean = ''.join(c for c in link_text if c.isprintable())
        
        if link_text != link_text_clean:
            print(f"{link_text} = {link_text_clean}")
        
        if link.get('href') == "#":
            continue
        
        if  link.get('rel') is not None and 'nofollow' in link.get('rel'):
            # print(f"nofollow: {link.get('href')}")
            continue
        
        text = f"{line}|{link_text_clean}|{link.get('href')}\n"
        all_links.append(text)

with open("pages.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line == "":
            continue
        
        print(line)
        process_link(line.strip())
        

with open("all_links.txt", "w", encoding="utf-8") as f:
    for entry in all_links:
        f.write(entry)