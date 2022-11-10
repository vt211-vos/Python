import random


class Coin:
    def __init__(self):
        self.counter = 0
        self.__sideUp = 'head'
    def Toss(self):
        self.counter += 1
        arr = ['head','tail']
        self.__sideUp = random.choice(arr)
    def __str__(self):
        return self.__sideUp
myCoin = Coin()
print(myCoin)
myCoin.Toss()
print(myCoin)
myCoin.Toss()
print(myCoin)
print(myCoin.counter)
