# BFS-DFS-Wikipedia-crawler
Web Crawler that uses BFS and DFS to get all wikipedia pages starting from a given seed page
The DFS crawler will consume two arguments: a URL and a keyword to be matched against anchor text or text within a URL.
Starting with the following seed URL from Wikipedia https://en.wikipedia.org/wiki/Tropical_cyclone
Follow the links with the prefix https://en.wikipedia.org/wiki that lead to articles only (avoid administrative)
Crawl to depth 6 and record the first 1000 webpages visited 