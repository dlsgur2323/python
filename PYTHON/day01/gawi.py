import random
arr = ["가위", "바위", "보"]
com = random.choice(arr)
user = input("가위, 바위, 보 !! ")

print("당신 : {} / 컴퓨터 : {}".format(user, com))

if com==user :
    print("비겼습니다!")
elif (com=="가위" and user=="바위") or (com=="바위" and user=="보") or (com=="보" and user=="가위") :
    print("당신이 이겼습니다!")
else :
    print("당신이 졌습니다.")
    