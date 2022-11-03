import datetime
from person import Person



dt = '2005-2-5'
Person1 = Person("Oleksandr", "Vyhnych", "qwe", datetime.datetime.strptime(dt, "%Y-%m-%d"))
print(Person1.nickname)
print(Person1.get_age())
print(Person1.get_fullname())