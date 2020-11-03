import requests
import bs4
import urllib
import pymysql

client_id = "gIeBFExnRjVvJ3jscFGJ"
client_secret = "r4tgfdrumS"
encText = urllib.parse.quote("대전 맛집")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
response_body = response.read()

bs = bs4.BeautifulSoup(response_body, "xml")
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


    
    
    
    
    