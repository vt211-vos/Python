class Apple:
    states = ["Відсутнє", "Цвітіння", "Зелене", "Червоне"]
    def __init__(self, index, state = states[0]):
        self.index = index
        self.state = state

    def grow(self):
        if self.state != "Червоне":
            self.state = self.states[self.states.index(self.state) +1]

    def  is_ripe(self):
        if self.state == "Червоне":
            return "Дозріло"
        return "Не дозріло"
    def __str__(self):
        return f"state=>{self.state} id=>{self.index}"

class AppleTree:
    def __init__(self, a):
        self.Apples = []
        self.Apples.extend(a)

    def grow_all(self):
        states = ["Відсутнє", "Цвітіння", "Зелене", "Червоне"]
        for i in self.Apples:
            i.state = states[states.index(i.state) + 1]

    def all_are_ripe(self):
        for i in self.Apples:
            if i.state != "Червоне":
                return "Не дозріло"

        return "дозріло"

    def give_away_all(self):
        self.Apples.clear()

class Gardener:
    def __init__(self, name, tree: AppleTree):
        self.name = name
        self._tree = tree
    def work(self):
        if self._tree.all_are_ripe() != 'дозріло':
            print("Ще не дозріло")
            for i in self._tree.Apples:
                i.grow()
        else:
            print("Збір")
            self._tree.give_away_all()

    def harvest(self):
        self._tree.all_are_ripe()

    def apple_base(self):
        print(len(self._tree.Apples))
        for i in self._tree.Apples:
            print(i)



a1 = Apple(1)
print(a1)
a2 = Apple(2)
print(a2)
a3 = Apple(3)
print(a3)
tr = AppleTree([a1,a2,a3])
gd = Gardener("Alex", tr)
gd.work()
gd.work()
gd.work()
gd.work()


