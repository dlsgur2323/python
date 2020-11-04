import threading

def num():
    for i in range(100000):
        print(i, end='\t')
        if((i+1)%100==0):
            print()

def ch():
    for i in range(100000):
        print(chr(i), end='\t')
        if((i+1)%100==0):
            print()
        
if __name__ == '__main__':
    th1 = threading.Thread(target=num)
    th2 = threading.Thread(target=ch)
    th1.start()
    th2.start()