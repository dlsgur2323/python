class Animal :
    def __init__(self):
        self.age = 1
    def getold(self) :
        self.age += 1

a = Animal()
print(a.age)
a.getold()
print(a.age)