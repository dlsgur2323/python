from os.path import sys

btn0 = 1
btn1 = 2
btn2 = 3

mod = sys.modules[__name__]

for idx in range(3) :
    print(getattr(mod,  'btn{}'.format(idx)))