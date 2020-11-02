class Animal :
    def __init__(self):
        self.age = 1
    def getold(self):
        self.age += 1

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.money_power = 1000000000000
    def earnMoney(self, i="none"):
        if i == 'none':
            self.money_power += 1
        else :
            self.money_power += i
    def getold(self):
        self.age += 2
        
if __name__ == '__main__':
    a = Human()
    print(a.age)
    print(a.money_power)
    a.getold()
    a.earnMoney()
    a.earnMoney(100000000)
    print(a.age)
    print(a.money_power)