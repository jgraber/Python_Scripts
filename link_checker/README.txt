Idea: LinkChecker

Problem to solve: Invalid links to no longer available content in my blogs

Alternatives: Great for massive sites who spend money on a service, massive options to create it on your own. The middleground lacks a useful, simple solution.

Approach 1:
- Read sitemap.xml
- Collect all pages with real content
- iterate through all pages and find all links
- uniquify all links (to check them only once)
- check the links
- create a report (link with error, what pages have it and how is the link text)