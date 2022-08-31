import requests
from typing import NamedTuple
import pprint

pp = pprint.PrettyPrinter(indent=5, depth=10, width=40, compact=False)

class Page(NamedTuple):
    url: str
    text: str


def read_links():
    with open("all_links.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        return lines
    
def prepare_targes(lines):
    targets = {}
    for line in lines:
        parts = line.split("|")
        target = parts[2].strip()
        page = Page(parts[0], parts[1])
        
        if target.startswith("#"):
            continue
        
        if not target.lower().startswith("http"):
            continue
        
        # print(target)
        if target in targets:
            targets[target].append(page)
        else:
            targets[target] = [page]
            
    return targets
   
    
def print_structure(targets):
    for key in targets:
        print(f"* {key}")
        for page in targets[key]:
            print(f"\t - {page.url} [{page.text}]")

def check_targets(targets):
    status = {}
    for key in targets:
        
        try:
            print(f"working on {key}")
            page = requests.head(key, timeout=5)
            code = page.status_code
        except ConnectionRefusedError:
            code = 'ConnectionRefusedError'
        except Exception:
            code = 'Exception'
            
        if code in status:
            # print(f"{code}:{key}")
            status[code].append(key)
        else:
            # print(f"{code}:{key}")
            status[code] = [key]
    return status

def print_status(status, targets):
    with open("report_links.txt", "w", encoding="utf-8") as f:
        for code in status:
            f.write(f"- {code}\n")
            for page in status[code]:
                f.write(f"\t - {page}\n")
                for source in targets[page]:
                    f.write(f"\t\t - {source.url} [{source.text}]\n")


if __name__ == '__main__':
    lines = read_links()
    targets = prepare_targes(lines)
    print(f"#targets: {len(targets)}")
    # print_structure(targets)
    status = check_targets(targets)
    print_status(status, targets)
    print("\n\nDone \n\n")
    