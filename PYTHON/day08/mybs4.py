import requests
import bs4

url = "http://finance.daum.net/api/quote/A005930/sectors"

response = requests.get(url)
response.encoding="utf-8"
html = response.text

bs = bs4.BeautifulSoup(html, "json")

print(bs)