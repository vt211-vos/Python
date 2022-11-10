class Pets:
    pets = []
    def Show(self):
        for i in self.pets:
            print(i)
class Dog(Pets):
    nature = ""
    breed = ""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.pets.append(self)
    def __str__(self):
        return (f"name:{self.name} age {self.age}")

    def behavior(self):
        return "Gaw"
class Akita(Dog):
    breed = "Akita"
    nature = "kind"
    def behavior(self):
        return "Gaaw"
class Terrier(Dog):
    breed = "Terrier"
    nature = "angry"
    def behavior(self):
        return "Gaaaw"

dog1 = Akita("qwe",5)
dog2 = Terrier("asd",6)
dog1.Show()