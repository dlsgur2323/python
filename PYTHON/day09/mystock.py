import requests
import bs4
import pymysql
from _datetime import datetime
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import threading

from_class = uic.loadUiType("samsung.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.click)
        self.code = "005930"
        self.name = "삼성전자"
        
        self.thre = threading.Thread(target=self.th)
    
    def click(self):
        self.thre.start()
        
    def th(self):
        while(True):
            db = pymysql.connect(host='localhost', port=3306,user='root',passwd='java', db='python_k', charset='utf8')
            cursor = db.cursor()
            
            now = datetime.now()
            nowDateTime = now.strftime("%Y-%m-%d %H:%M")
            
            url = "https://finance.naver.com/item/sise.nhn?code="+self.code
            response = requests.get(url)
            html = response.text
            
            bs = bs4.BeautifulSoup(html, "lxml")
            p = bs.select("p.no_today")
            
            if(len(p) > 0 ):
                span = p[0].select("span")
                price = span[0].text
                
                sql = "INSERT INTO stock (cname, ccode, price, gtime) VALUES (%s, %s, %s, %s)"
                
                cursor.execute(sql, (self.name, self.code, price, nowDateTime))
                self.lbl.setText(price + " - " + nowDateTime)
            db.commit()
            db.close()
            time.sleep(60)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()







    
    




