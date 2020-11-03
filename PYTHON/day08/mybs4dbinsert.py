import requests
import bs4
import pymysql

url = "http://192.168.43.123/JAVASCRIPT/list.html"

response = requests.get(url)
response.encoding="utf-8"
html = response.text

bs = bs4.BeautifulSoup(html, "lxml")
tag = bs.select("tr")

db = pymysql.connect(host='localhost', port=3306,user='root',passwd='java', db='python_k', charset='utf8')

cursor = db.cursor()

sql = "INSERT INTO japanlist (jname, jaddr) VALUES (%s, %s)"

for p in tag :
    cursor.execute(sql, (p.select("td")[0].text, p.select("td")[1].text))

db.commit()
db.close()
