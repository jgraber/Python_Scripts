# pip install ultimate-sitemap-parser
# https://github.com/mediacloud/ultimate-sitemap-parser

from usp.tree import sitemap_tree_for_homepage
tree = sitemap_tree_for_homepage('https://improveandrepeat.com/')

with open("pages.txt", "w") as f:
    for page in tree.all_pages():
        f.write(f"{page.url}\n")