urls = []

with open("pages.txt", "r") as x:
    while True:
        line = x.readline()
        if not line:
            break
        urls.append(line)

print(f"Urls: {len(urls)}")

cleaned = set(urls)

print(f"Urls: {len(cleaned)}")

cleaned_list = list(cleaned)
cleaned_list.sort()

with open("pages_cleaned.txt", "w") as f:
    for page in cleaned_list:
        f.write(f"{page}")