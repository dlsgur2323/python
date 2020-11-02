import random
from sympy.core.evalf import rnd

mine = input("홀/짝을 입력하세요 : ")
rnd = random.random()
com = ""
result = ""
if rnd>=0.5 :
    com="홀"
else :
    com="짝"

if mine==com :
    print("당신 : {} / 컴퓨터 : {}".format(mine, com))
    print("이겼습니다.")
else :
    print("당신 : {} / 컴퓨터 : {}".format(mine, com))
    print("졌습니다.")
    