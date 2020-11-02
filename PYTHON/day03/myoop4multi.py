class Animal :
    def __init__(self):
        self.age = 1
    def getold(self):
        self.age += 1
        
class God :
    def __init__(self):
        self.spirit_power = 1
    def goToGeryong(self):
        self.spirit_power += 10
    def goToMinsokchon(self):
        self.spirit_power += 2
        
    
class Human(Animal, God):
    def __init__(self): #생성자 __init(self)
        Animal.__init__(self)
        God.__init__(self)
        self.money_power = 1000000000000
    def earnMoney(self, i="none"):
        if i == 'none':
            self.money_power += 1
        else :
            self.money_power += i
    def getold(self):
        self.age += 2
    def __str__(self):  #toString
        return str(self.age) + " : " + str(self.money_power) + " : " + str(self.spirit_power)
    
if __name__ == '__main__':
    a = Human()
    print(a)
    a.getold()
    a.earnMoney()
    a.earnMoney(100000000)
    a.goToGeryong()
    a.goToMinsokchon()
    print("-------------------after---------------------")
    print(a)
    