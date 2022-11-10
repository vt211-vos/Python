import math


class Bank:
    def __init__(self, balance = 100):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    def putOn(self, sum):
        if sum > 0:
            self.__balance += sum
            print(f"На рахунок зараховано => {sum}")
        else: print("Сума має бути більше 0")
    def withDraw(self, sum):
        if math.fabs(sum) <= self.__balance:
            self.__balance -= sum
            print(f"На рахунок зараховано => {sum}")
        else: print('Сума має бути менша наж поточний балансе')
    def  __str__(self):
        return (f"Поточний баланс => {self.__balance}")
person = Bank(400)
print(person)
person.putOn(200)
person.withDraw(500)
print(person)

