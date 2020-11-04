from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5 import uic
import sys
import time
import threading

from_class = uic.loadUiType("thread.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.click)
    
    def click(self):
        thre = threading.Thread(target=self.th)
        thre.start()
        
    def th(self):
        for i in range(10):
            time.sleep(1)
            num = int(self.lbl.text())
            num += 1
            self.lbl.setText(str(num))
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
