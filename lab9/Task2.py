class House:
    def __init__(self, area=100, price=100):
        self.area = area
        self.price = price
    def final_price(self, discount):
        return self.price * (1-(discount/100))
    def __str__(self):
        return (f"area=>{self.area} price=>{self.price}")
class SmallHouse(House):
    def __init__(self, price = 100):
        self.area = 40
        self.price = price
class Human:
    default_name = "Name"
    default_age = 101
    def __init__(self, money, house, name=default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house
    def info(self):
        print(f"money=>{self.__money} house=>{self.__house} name=>{self.name} age=>{self.age}")

    @staticmethod
    def defaulte_info():
        print(f"name=>{Human.default_name} age=>{Human.default_age}")


    def __make_deal(self, price):
        self.__money -= price

    def earn_money(self, money):
        self.__money += money

    def buy_house(self, house, discount =10):
        if self.__money < house.price:
            print("Грошей не достатньо")
        else:
            price = house.final_price(discount)
            self.__make_deal(price)
            print("Куплено")



Human.defaulte_info()
house = House(200, 200_000)
testHuman = Human(50_000, house)
testHuman.info()
sh = SmallHouse(100_000)
testHuman.buy_house(sh)
testHuman.earn_money(500_000)
testHuman.buy_house(sh)
testHuman.info()