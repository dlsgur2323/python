'''
    1~100 까지의 수에서 3의 배수의 합을 구해라?
'''
sum = 0
for i in range(1,101) :
    if i%3 == 0 :
        sum += i
print(sum)