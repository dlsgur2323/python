import pygame
import sys
from numba.tests.test_flow_control import try_except_usecase
from PyQt5.QtWidgets import QMessageBox
from tkinter import *
from tkinter import messagebox

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255, 255, 255)
gray = (100,100,100)
black = (0, 0, 0)

b1 = (255, 0, 0)
b2 = (245, 0, 0)
b3 = (235, 0, 0)
b4 = (225, 0, 0)
b5 = (215, 0, 0)
b6 = (205, 0, 0)
b7 = (195, 0, 0)

s1 = (0, 0, 255)
s2 = (0, 0, 245)
s3 = (0, 0, 235)
s4 = (0, 0, 225)
s5 = (0, 0, 215)
s6 = (0, 0, 205)
s7 = (0, 0, 195)


Tk().wm_withdraw()
pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 200
pos_y = 10
mission_cnt = 2
flag_ing = True


block2D = [
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]
]
 
stack2D = [
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[11,11,11,11,11,11,0,0,0,0]
] 
print2D = [
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]
] 

class Block:
    def __init__(self) :
        self.kind = 1
        self.status = 0
        self.i = 2
        self.j = 4
    def __str__(self) :
        return "kind : "+ str(self.kind) + " status : "+ str(self.status) + " i : " + str(self.i) + " j : " + str(self.j)
        
block = Block()

def setPrint2DByBlockStack() :
    for i in range(len(block2D)) :
        for j in range(len(block2D[i])) :
            if block2D[i][j] != 0 :
                print2D[i][j] = block2D[i][j]
            
            if stack2D[i][j] != 0 : 
                print2D[i][j] = stack2D[i][j]

def setBlock2DByBlock() :
    for i in range(len(block2D)) :
        for j in range(len(block2D[i])) :
            block2D[i][j] = 0
            print2D[i][j] = 0
                
    if block.kind==1 : # 네모
        block2D[block.i         ][block.j          ] = block.kind
        block2D[block.i+1       ][block.j          ] = block.kind
        block2D[block.i         ][block.j+1        ] = block.kind
        block2D[block.i+1       ][block.j+1        ] = block.kind
        
    elif block.kind==2 : # 지그재그1
        if block.status==0 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i-1    ][block.j          ] = block.kind
            block2D[block.i      ][block.j-1        ] = block.kind
            block2D[block.i+1    ][block.j-1        ] = block.kind
        if block.status==1 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i      ][block.j+1        ] = block.kind
            block2D[block.i-1    ][block.j          ] = block.kind
            block2D[block.i-1    ][block.j-1        ] = block.kind
        
    elif block.kind==3 : # 지그재그2
        if block.status==0 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i-1    ][block.j          ] = block.kind
            block2D[block.i      ][block.j+1        ] = block.kind
            block2D[block.i+1    ][block.j+1        ] = block.kind
        if block.status==1 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i      ][block.j+1        ] = block.kind
            block2D[block.i+1    ][block.j          ] = block.kind
            block2D[block.i+1    ][block.j-1        ] = block.kind
        
    elif block.kind==4 : # 막대
        if block.status==0 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i      ][block.j+1        ] = block.kind
            block2D[block.i      ][block.j-1        ] = block.kind
            block2D[block.i      ][block.j-2        ] = block.kind
        if block.status==1 :
            block2D[block.i+2    ][block.j          ] = block.kind
            block2D[block.i+1    ][block.j          ] = block.kind
            block2D[block.i-1    ][block.j          ] = block.kind
            block2D[block.i      ][block.j          ] = block.kind
        
    elif block.kind==5 : # ㅗ
        if block.status==0 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i-1    ][block.j          ] = block.kind
            block2D[block.i      ][block.j-1        ] = block.kind
            block2D[block.i      ][block.j+1        ] = block.kind
        if block.status==1 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i-1    ][block.j          ] = block.kind
            block2D[block.i+1    ][block.j          ] = block.kind
            block2D[block.i      ][block.j+1        ] = block.kind
        if block.status==2 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i+1    ][block.j          ] = block.kind
            block2D[block.i      ][block.j-1        ] = block.kind
            block2D[block.i      ][block.j+1        ] = block.kind
        if block.status==3 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i-1    ][block.j          ] = block.kind
            block2D[block.i+1    ][block.j          ] = block.kind
            block2D[block.i      ][block.j-1        ] = block.kind
            
    elif block.kind==6 : # ㄱ
        if block.status==0 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i-1    ][block.j          ] = block.kind
            block2D[block.i+1    ][block.j          ] = block.kind
            block2D[block.i-1    ][block.j-1        ] = block.kind
        if block.status==1 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i      ][block.j-1        ] = block.kind
            block2D[block.i      ][block.j+1        ] = block.kind
            block2D[block.i-1    ][block.j+1        ] = block.kind
        if block.status==2 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i+1    ][block.j          ] = block.kind
            block2D[block.i-1    ][block.j          ] = block.kind
            block2D[block.i+1    ][block.j+1        ] = block.kind
        if block.status==3 :
            block2D[block.i      ][block.j+1        ] = block.kind
            block2D[block.i      ][block.j-1        ] = block.kind
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i+1    ][block.j-1        ] = block.kind
        
    elif block.kind==7 : # ㄴ
        if block.status==0 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i+1    ][block.j          ] = block.kind
            block2D[block.i-1    ][block.j          ] = block.kind
            block2D[block.i-1    ][block.j+1        ] = block.kind
        if block.status==1 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i      ][block.j-1        ] = block.kind
            block2D[block.i      ][block.j+1        ] = block.kind
            block2D[block.i+1    ][block.j+1        ] = block.kind
        if block.status==2 :
            block2D[block.i-1    ][block.j          ] = block.kind
            block2D[block.i+1    ][block.j          ] = block.kind
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i+1    ][block.j-1        ] = block.kind
        if block.status==3 :
            block2D[block.i      ][block.j          ] = block.kind
            block2D[block.i      ][block.j+1        ] = block.kind
            block2D[block.i      ][block.j-1        ] = block.kind
            block2D[block.i-1    ][block.j-1        ] = block.kind


def show2D(arr) :
    for i in arr :
        print(i)
    print("=================================")

def myrender() :
    screen.fill(gray)
    
    font = pygame.font.Font("cmss10.ttf",30)
    text =font.render(str(mission_cnt),True,(28,0,0))
    screen.blit(text,(10,10))
    
    for i in range(len(block2D)) :
        for j in range(len(block2D[i])) :
            if print2D[i][j] == 0 : pygame.draw.rect(screen, white, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 1 : pygame.draw.rect(screen, b1, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 2 : pygame.draw.rect(screen, b2, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 3 : pygame.draw.rect(screen, b3, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 4 : pygame.draw.rect(screen, b4, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 5 : pygame.draw.rect(screen, b5, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 6 : pygame.draw.rect(screen, b6, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 7 : pygame.draw.rect(screen, b7, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 11 : pygame.draw.rect(screen, s1, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 12 : pygame.draw.rect(screen, s1, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 13 : pygame.draw.rect(screen, s1, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 14 : pygame.draw.rect(screen, s1, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 15 : pygame.draw.rect(screen, s1, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 16 : pygame.draw.rect(screen, s1, (pos_x+(j*20), pos_y+(i*20), 19, 19))
            if print2D[i][j] == 17 : pygame.draw.rect(screen, s1, (pos_x+(j*20), pos_y+(i*20), 19, 19))
    
    pygame.display.update()

def changeStatus() :
                if block.kind==1 :
                    pass
                if block.kind==2 or block.kind==3 or block.kind==4 :
                    if block.status==0 :
                        block.status = 1
                    elif block.status==1 :
                        block.status = 0
                if block.kind==5 or block.kind==6 or block.kind==7 :
                    if block.status==0 :
                        block.status = 1
                    elif block.status==1 :
                        block.status = 2
                    elif block.status==2 :
                        block.status = 3
                    elif block.status==3 :
                        block.status = 0

def isCrash() :
    for i in range(len(block2D)) :
        for j in range(len(block2D[i])) :
            if(block2D[i][j] > 0 and stack2D[i][j] > 0) :
                return True;
    return False;

def moveBlock2Stack() :
    for i in range(len(block2D)) :
        for j in range(len(block2D[i])) :
            if(block2D[i][j] > 0) :
                stack2D[i][j] = block2D[i][j] + 10;
def remove10():
    arrTemp = []
    cnt10 = 0;
    for i in range(len(stack2D)) :
        if(stack2D[i][0] > 0 and
            stack2D[i][1] > 0 and
            stack2D[i][2] > 0 and
            stack2D[i][3] > 0 and
            stack2D[i][4] > 0 and
            stack2D[i][5] > 0 and
            stack2D[i][6] > 0 and
            stack2D[i][7] > 0 and
            stack2D[i][8] > 0 and
            stack2D[i][9] > 0) :
            cnt10 +=1
        else :
            arrTemp.append(stack2D[i])
            
    for i in range(cnt10) :
        arrTemp.insert(0,[0,0,0,0,0,0,0,0,0,0]);
    
    for i in range(len(arrTemp)) :
        stack2D[i] = arrTemp[i]

    
    return cnt10;

clock = pygame.time.Clock()
while True:
    clock.tick(10)
    
    if not flag_ing :
        continue
    
    cntkey=0
    flag_render = False
    
    flagOut = False
    flagCrash = False
    flagDown = False
    pre_i = block.i
    pre_j = block.j
    pre_status = block.status
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        block.j -= 1
        flag_render = True
        cntkey+=1
        
    if key_event[pygame.K_RIGHT]:
        block.j += 1
        flag_render = True
        cntkey+=1

    if key_event[pygame.K_UP]:
        changeStatus()
        flag_render = True
        cntkey+=1

    if key_event[pygame.K_DOWN]:
        block.i += 1
        flag_render = True
        flagDown = True
        cntkey+=1
    
    if key_event[pygame.K_d]:   
        print(block)
        show2D(block2D)
        show2D(print2D)
        cntkey+=1
    
    
    
    if flag_render :
        
        try:
            block.j -= 10
            setBlock2DByBlock()
            block.j += 10
            setBlock2DByBlock()
        except:
            flagOut = True;
        
        flagCrash = isCrash()
    
        if flagOut or flagCrash :
            block.i = pre_i
            block.j = pre_j
            block.status = pre_status
            setBlock2DByBlock()
            if flagDown :
                moveBlock2Stack();
                block.i = 2;
                block.j = 4;
                block.status = 0;
                setBlock2DByBlock();
                
                if(stack2D[5][0] >0 or stack2D[5][1] >0 or stack2D[5][2] >0 or
                   stack2D[5][3] >0 or stack2D[5][4] >0 or stack2D[5][5] >0 or
                   stack2D[5][6] >0 or stack2D[5][7] >0 or stack2D[5][8] >0 or
                   stack2D[5][9] >0) :
                    
                    flag_ing = False;
                    messagebox.showinfo('Tetris', 'you lose~~')

                cnt10 = remove10();
                if cnt10>0:
                    mission_cnt -= cnt10
                    if(mission_cnt <=0):
                        messagebox.showinfo('Tetris', 'you win!!')
                
        setPrint2DByBlockStack()
        myrender()
    
        
        
       # screen.fill(black)
        #pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
        #pygame.display.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    