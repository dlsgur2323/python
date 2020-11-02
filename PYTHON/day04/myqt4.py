from os.path import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from_class = uic.loadUiType("pyqt5.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_1.clicked.connect(self.click)
        self.btn_2.clicked.connect(self.click)
        self.btn_3.clicked.connect(self.click)
        self.btn_4.clicked.connect(self.click)
        self.btn_5.clicked.connect(self.click)
        self.btn_6.clicked.connect(self.click)
        self.btn_7.clicked.connect(self.click)
        self.btn_8.clicked.connect(self.click)
        self.btn_9.clicked.connect(self.click)
        self.btn_0.clicked.connect(self.click)
        self.call.clicked.connect(self.calling)
    
    def click(self):
        i = self.sender().text();
        t = self.le.text();
        self.le.setText(t+i);
        
    def calling(self):
        i = self.le.text();
        QMessageBox.about(self, "calling~", "tel : " + i +"\ncalling")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
