from os.path import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from_class = uic.loadUiType("hello.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        self.lbl.setText("Good Afternoon")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
