print('Введіть цілі числа')
x1 = int(input())
x2 = int(input())
print('Введіть дробові числа')
y1 = float(input())
y2 = float(input())
print("перше -" + str(x1) + " друге -" + str(x2) + " третє -" + str(y1) +
      " четверте -" + str(y2))

list = [x1+x2, x1-x2, x1*x2, x1/x2, x1**x2, x1%x2]
print(list)
print('кількість елементів списку')
print(len(list))
print('парні елементи')
for i in range(len(list)):
        if(list[i]%2 == 0):
            print(list[i])
print('/////////')
print(list)
temp = list[2]
list[2] = list[5]
list[5] = temp
print(list)

print("Введіть прізвище та ім'я")
name = input()
print('Виконав ' + name)
print('Висновок:на даній лабораторній роботі було\n'+
      ' проведено повторення та ознайомлення з основами\n'+
      ' мови програмування Python. Виконано базові дії над\n'+
      ' операторами та функціями даної мови програмування. Роботу\n'+
      ' виконано в повному обсязі.')
