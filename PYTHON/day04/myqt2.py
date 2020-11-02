from os.path import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from_class = uic.loadUiType("pyqt2.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        i = int(self.le.text())
        self.le.setText(str(i+1))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
