from os.path import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from_class = uic.loadUiType("pyqt4.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        arr = [int(self.le1.text()), int(self.le2.text())]
        mn = min(arr)
        mx = max(arr)
        sum = int((mn + mx) * (mx-mn+1) / 2)
        self.le3.setText(str(sum))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
