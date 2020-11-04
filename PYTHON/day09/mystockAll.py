import requests
import bs4
import pymysql
from _datetime import datetime
import threading

#------------------------  DB, 날짜 설정 ---------------------------
now = datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M")

#------------------------  종목코드 추출  ---------------------------
print("코드추출 작업 시작")
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
print("코드추출 작업 완료")

#------------------------  종목 정보 크롤링 작업  ---------------------------
def work(a,b,c):
    print(str(c)+"번 쓰레드 작업 시작")
    print("작업할 양 : "+ str(b-a+1))
    db = pymysql.connect(host='localhost', port=3306,user='root',passwd='java', db='python_k', charset='utf8')
    cursor = db.cursor()
    
    for i in range(a,b):
        ar = codes[i]
        code = ar[1]
        name = ar[0]
    
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
            db.commit()
        print(str(c)+"번 쓰레드  " + str(i)+"번째 작업 완료, 남은 작업 수 : " + str(b-(i+1)))
        
    print(str(c)+"번 쓰레드 완료")
    db.close()
    
print("크롤링 시작")
th1 = threading.Thread(target=work, args=(0,500,1))
th2 = threading.Thread(target=work, args=(500,1000,2))
th3 = threading.Thread(target=work, args=(1000,1500,3))
th4 = threading.Thread(target=work, args=(1500,2000,4))
th5 = threading.Thread(target=work, args=(2000,2500,5))
th6 = threading.Thread(target=work, args=(2500,l,6))
th1.start()
th2.start()
th3.start()
th4.start()
th5.start()
th6.start()




