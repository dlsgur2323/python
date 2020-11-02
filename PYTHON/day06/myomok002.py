from os.path import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow,\
    QMessageBox
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
        self.play= True
        for i in range(len(self.arr2D)):
            line = []
            for j in range(len(self.arr2D[i])):
                btn = QtWidgets.QPushButton(self)
                btn.setGeometry(j*40, i*40, 40, 40)
                btn.setAccessibleName(str(i)+","+str(j))
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QSize(40,40));
                btn.clicked.connect(self.btn_clicked)
                line.append(btn)
            self.btn2D.append(line)
        self.reset.clicked.connect(self.btn_reset)
    
    def btn_reset(self):
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
        self.play = True
        self.turn = True
        self.myrender()
    def myrender(self):
        for i in range(len(self.arr2D)):
            for j in range(len(self.arr2D[i])):
                if self.arr2D[i][j]==0 :
                    self.btn2D[i][j].setIcon(QtGui.QIcon("0.png"))
                elif self.arr2D[i][j]==1 :
                    self.btn2D[i][j].setIcon(QtGui.QIcon("1.png"))
                elif self.arr2D[i][j]==2 :
                    self.btn2D[i][j].setIcon(QtGui.QIcon("2.png"))
            
    def btn_clicked(self):
        if not self.play :
            return
        geo = self.sender().accessibleName().split(",")
        y = int(geo[0])
        x = int(geo[1])
        if self.arr2D[y][x] == 0 :
            if self.turn : 
                self.arr2D[y][x] = 1
                color = 1
            else :
                self.arr2D[y][x] = 2
                color = 2
        self.myrender()
        cntUp = self.getUp(y,x,color)
        cntDw = self.getDw(y,x,color)
        cntLe = self.getLe(y,x,color)
        cntRi = self.getRi(y,x,color)
        cntUr = self.getUr(y,x,color)
        cntUl = self.getUl(y,x,color)
        cntDr = self.getDr(y,x,color)
        cntDl = self.getDl(y,x,color)
        
        cntUd = cntUp + cntDw
        cntRl = cntRi + cntLe
        cntcr1 = cntUl + cntDr
        cntcr2 = cntUr + cntDl
        
        if cntUd == 4 or cntRl == 4 or cntcr1 == 4 or cntcr2 == 4 :
            if self.turn :
                QMessageBox.about(self, "결과", "백돌이 이겼습니다.")
            else :
                QMessageBox.about(self, "결과", "흑돌이 이겼습니다.")
            self.play = False;
         
            
        
        
        self.turn = not self.turn 
    
    def getUp(self, i, j,color):
        cnt = 0
        try:
            while(i>0) :
                i -= 1
                if(self.arr2D[i][j]==color):
                    cnt += 1
                else :
                    break
        except :
            pass
        return cnt
    
    def getDw(self, i, j,color):
        cnt = 0
        try:
            while(True) :
                i += 1
                if(self.arr2D[i][j]==color):
                    cnt += 1
                else :
                    break
        except :
            pass
        return cnt
    
    def getLe(self, i, j,color):
        cnt = 0
        try:
            while(True) :
                j -= 1
                if(self.arr2D[i][j]==color):
                    cnt += 1
                else :
                    break
        except :
            pass
        return cnt
    
    def getRi(self, i, j,color):
        cnt = 0
        try:
            while(True) :
                j += 1
                if(self.arr2D[i][j]==color):
                    cnt += 1
                else :
                    break
        except :
            pass
        return cnt
    
    def getUr(self, i, j,color):
        cnt = 0
        try:
            while(True) :
                i -= 1
                j += 1
                if(self.arr2D[i][j]==color):
                    cnt += 1
                else :
                    break
        except :
            pass
        return cnt
    
    def getUl(self, i, j,color):
        cnt = 0
        try:
            while(True) :
                i -= 1
                j -= 1
                if(self.arr2D[i][j]==color):
                    cnt += 1
                else :
                    break
        except :
            pass
        return cnt
    
    def getDl(self, i, j,color):
        cnt = 0
        try:
            while(True) :
                i += 1
                j -= 1
                if(self.arr2D[i][j]==color):
                    cnt += 1
                else :
                    break
        except :
            pass
        return cnt
    
    def getDr(self, i, j,color):
        cnt = 0
        try:
            while(True) :
                i += 1
                j += 1
                if(self.arr2D[i][j]==color):
                    cnt += 1
                else :
                    break
        except :
            pass
        return cnt
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()











