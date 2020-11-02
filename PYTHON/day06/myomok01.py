from os.path import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from idlelib.debugobj import myrepr

from_class = uic.loadUiType("omok.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.arr2D = [
                        [1,0,0,0,0,0,0,0,0,0],
                        [0,1,2,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0]
                    ]
        self.lbl2D= []
        
        for i in range(len(self.arr2D)):
            line = []
            for j in range(len(self.arr2D[i])):
                label = QtWidgets.QLabel(self)
                label.setGeometry(j*40, i*40, 41, 41)
                label.setPixmap(QtGui.QPixmap("0.png"))
                line.append(label)
            self.lbl2D.append(line)
        self.setupUi(self)
        self.myrender()
        
        
    def myrender(self):
        for i in range(len(self.arr2D)):
            for j in range(len(self.arr2D[i])):
                if self.arr2D[i][j]==0 :
                    self.lbl2D[i][j].setPixmap(QtGui.QPixmap("0.png"))
                elif self.arr2D[i][j]==1 :
                    self.lbl2D[i][j].setPixmap(QtGui.QPixmap("1.png"))
                elif self.arr2D[i][j]==2 :
                    self.lbl2D[i][j].setPixmap(QtGui.QPixmap("2.png"))
            
    def btn_clicked(self):
        self.printArr2D();
        
    def printArr2D(self):
        for i in range(len(self.arr2D)):
            print(self.arr2D[i])
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
