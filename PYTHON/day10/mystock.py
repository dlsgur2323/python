import requests
import bs4
import pymysql
from _datetime import datetime
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import threading

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

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
            
            options = Options()
            options.headless = True
            browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
            browser.get("https://finance.daum.net/quotes/A005930")
            
            tag = browser.find_element_by_css_selector("#boxSummary > div > span:nth-child(1) > span.currentB > span.numB.up > strong")
            
            price = tag.text
            
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







    
    




