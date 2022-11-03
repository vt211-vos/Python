import datetime
class Person:
    def __init__(self, surname, first_name, nickname, birth_date):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        self.birth_date = birth_date
    def get_age(self):
        ageF = datetime.datetime.now() - self.birth_date
        age =  ageF.days / 365.2425
        return str(int(age))
    def get_fullname(self):
        return f"{self.first_name} {self.surname}"
    def modifier(filename):
        with open('filename', 'r', encoding='utf8') as file:
            data = file.readlines()
        info = [i.replace("\n", "") for i in data]
        person = Person(info[0], info[1], info[2], datetime.datetime.strptime(info[3], "%Y-%m-%d"))
        print(person.get_age())

        with open(filename, 'w', encoding='utf8') as file:
            file.write("")
        with open(filename, 'a', encoding='utf8') as file:
            for i in range(len(data)):
                if i == 2:
                    file.write(person.get_fullname() + '\n')
                file.write(data[i])
            file.write("\n" + person.get_age())