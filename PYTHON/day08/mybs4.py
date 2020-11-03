import requests
import bs4

url = "http://192.168.43.123/JAVASCRIPT/list.html"

response = requests.get(url)
response.encoding="utf-8"
html = response.text

bs = bs4.BeautifulSoup(html, "lxml")
tags = bs.select("td")
for p in tags:
    print(p.text)