import requests
import bs4
import pymysql
from _datetime import datetime
import time

db = pymysql.connect(host='localhost', port=3306,user='root',passwd='java', db='python_k', charset='utf8')
        
cursor = db.cursor()
print("작업 시작")
url = "https://www.ktb.co.kr/trading/popup/itemPop.jspx"
response = requests.get(url)
html = response.text

bs = bs4.BeautifulSoup(html, "lxml")
tbody = bs.select("tbody")
trs = tbody[0].select("tr")

codes = []
for tr in trs:
    td = tr.select("td")
    code = td[0].text
    name = td[1].text.rstrip()
    arr = [name, code]
    codes.append(arr)
    
l = len(codes)

for ar in codes:
    if(ar[0]=="삼성전자"):
        code = ar[1]
        name = ar[0]
        
while(True):
    db = pymysql.connect(host='localhost', port=3306,user='root',passwd='java', db='python_k', charset='utf8')
    cursor = db.cursor()
    
    now = datetime.now()
    nowDateTime = now.strftime("%Y-%m-%d %H:%M")
    
    url = "https://finance.naver.com/item/sise.nhn?code="+code
    response = requests.get(url)
    html = response.text
    
    bs = bs4.BeautifulSoup(html, "lxml")
    p = bs.select("p.no_today")
    
    if(len(p) > 0 ):
        span = p[0].select("span")
        price = span[0].text
        
        sql = "INSERT INTO stock (cname, ccode, price, gtime) VALUES (%s, %s, %s, %s)"
        
        cursor.execute(sql, (name, code, price, nowDateTime))
        
    print("작업 완료  -  "+nowDateTime)
    db.commit()
    db.close()
    time.sleep(60)


    
    




