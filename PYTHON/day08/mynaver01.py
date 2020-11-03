import requests
import bs4
import pymysql
from bs4 import BeautifulSoup


xml = open("naver.xml", "r", encoding="utf-8")

bs = BeautifulSoup(xml, "xml")

db = pymysql.connect(host='localhost', port=3306,user='root',passwd='java', db='python_k', charset='utf8')

cursor = db.cursor()

sql = "INSERT INTO naver (title, link, description, bloggername, bloggerlink, postdate) VALUES (%s, %s, %s, %s, %s, %s)"

items = bs.select("item")
for p in items :
    title = p.select("title")[0].text
    link = p.select("link")[0].text
    description = p.select("description")[0].text
    bloggername = p.select("bloggername")[0].text
    bloggerlink = p.select("bloggerlink")[0].text
    postdate = p.select("postdate")[0].text
    
    cursor.execute(sql, (title, link, description, bloggername, bloggerlink, postdate))


db.commit()
db.close()
