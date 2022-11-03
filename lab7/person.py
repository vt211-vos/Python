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