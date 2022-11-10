class Car:
    def __init__(self, brend, model, speed  = 0):
        self.brend = brend
        self.model = model
        self.speed = speed
    def accelerate(self):
        self.speed += 5
    def brake(self):
        self.speed -= 5
    def getSpeed(self):
        return self.speed

mycar = Car("Tesla", "x", 100)
print(f"Speed => {mycar.getSpeed()}")
for i in range(3):
    mycar.accelerate()
    print(f"accelerate{i}  speed => {mycar.getSpeed()}")
for i in range(3):
    mycar.brake()
    print(f"break{i}  speed => {mycar.getSpeed()}")

