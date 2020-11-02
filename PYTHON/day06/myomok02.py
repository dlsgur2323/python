from os.path import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5 import uic, QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from idlelib.debugobj import myrepr
from PyQt5.Qt import QSize

from_class = uic.loadUiType("omok.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.arr2D = [
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0]
                    ]
        self.setupUi(self)
        self.btn2D = []
        self.turn = True
        for i in range(len(self.arr2D)):
            line = []
            for j in range(len(self.arr2D[i])):
                btn = QtWidgets.QPushButton(self)
                btn.setGeometry(j*40, i*40, 40, 40)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QSize(40,40));
                btn.clicked.connect(lambda state, x=j, y=i : self.btn_clicked(state,x,y))
                line.append(btn)
            self.btn2D.append(line)
        
        
    def myrender(self):
        for i in range(len(self.arr2D)):
            for j in range(len(self.arr2D[i])):
                if self.arr2D[i][j]==0 :
                    self.btn2D[i][j].setIcon(QtGui.QIcon("0.png"))
                elif self.arr2D[i][j]==1 :
                    self.btn2D[i][j].setIcon(QtGui.QIcon("1.png"))
                elif self.arr2D[i][j]==2 :
                    self.btn2D[i][j].setIcon(QtGui.QIcon("2.png"))
            
    def btn_clicked(self, state, x, y):
        if self.turn :
            self.arr2D[y][x] = 1
            self.turn = False
        else:
            self.arr2D[y][x] = 2
            self.turn = True
        self.myrender()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
