import requests
import bs4

url = "https://www.ktb.co.kr/trading/popup/itemPop.jspx"
response = requests.get(url)
html = response.text

bs = bs4.BeautifulSoup(html, "lxml")
tbody = bs.select("tbody")
trs = tbody[0].select("tr")
for tr in trs:
    td = tr.select("td")
    #code = td[0].text
    #name = td[1].seleect("a")[0].text.trim()
    print(td[0].text, td[1].text)

