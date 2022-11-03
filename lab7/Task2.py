from person import Person
import datetime
with open('info.txt', 'r', encoding='utf8') as file:
    data = file.readlines()
info = [i.replace("\n", "") for i in data]
person = Person(info[0], info[1], info[2], datetime.datetime.strptime(info[3], "%Y-%m-%d"))
print(person.get_age())

with open('info.txt', 'w', encoding='utf8') as file:
    file.write("")
with open('info.txt', 'a', encoding='utf8') as file:
    for i in range(len(data)):
        if i == 2:
            file.write(person.get_fullname() + '\n')
        file.write(data[i])
    file.write("\n"+person.get_age())



