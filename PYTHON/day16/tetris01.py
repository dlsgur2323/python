import pygame
import sys
from numba.tests.test_flow_control import try_except_usecase

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255, 255, 255)
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


pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 200
pos_y = 10

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
        self.kind = 5
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
    screen.fill(black)

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



clock = pygame.time.Clock()
while True:
    clock.tick(10)
    flag_render = False
    flagOut = False
    flagCrash = False
    
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
        
    if key_event[pygame.K_RIGHT]:
        block.j += 1
        flag_render = True

    if key_event[pygame.K_UP]:
        changeStatus()
        flag_render = True

    if key_event[pygame.K_DOWN]:
        block.i += 1
        flag_render = True
    
    if key_event[pygame.K_d]:   
        print(block)
        show2D(block2D)
        show2D(print2D)
    
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
            
        setPrint2DByBlockStack()
        myrender()
    
        
        
       # screen.fill(black)
        #pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
        #pygame.display.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    