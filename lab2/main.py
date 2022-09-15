import math
def Task1():
    list = []
    for i in range(3):
        list.append(int(input()))
    for i in range(3):
        if list[i] >= 1 and list[i] <= 3:
            print(list[i])

def Task2():
    year = int(input())
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            print('366')
        elif year % 100 != 0:
            print('366')
        else:
            print('365')
    else:
        print('365')

def Task3():
    amount = int(input())
    if amount >= 500 and amount < 1000:
        amount -= amount/100*3
    if amount >= 1000:
        amount -= amount / 100 * 5
    print(amount)

def Task4():
    list = []
    for i in range(4):
        list.append(int(input()))

    print(math.cos(min(list)))

def Task5():
    list = []
    for i in range(3):
        list.append(int(input()))

    print(math.sin(max(list)))

def Task6():
    hight = int(input())
    width = int(input())
    s = hight*width/2
    if s % 2 == 0:
        s /= 2
    else:
        print("Не можу ділити на 2")

def Task7():
    list = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    x = int(input())
    if x >= 1 and x <= 12:
        print(list[x-1])
    else:
        print('x < 1 or x > 12')

def Task8():
    number = 0
    list = []
    for i in range(3):
        list.append(int(input()))
        if list[i] > 0:
            number += 1
    print(number)

def Task9():
    a = int(input())
    b = int(input())

    amount = 0
    for i in range(b-a+1):
        amount += a
        a += 1
    print(amount)

def Task10():
    a = int(input())
    b = int(input())

    amount = 0
    for i in range(b-a+1):
        amount += math.pow(a,2)
        a += 1
    print(amount)

def Task11():
    a = int(input())
    amount = 0
    if a > 200:
        print('число не має бути >= 200')
    else:
        sum = 200 - a + 1
        for i in range(sum):
            amount += a
            a += 1
        rez = amount/sum
        print(rez)

def Task12():
    a = int(input())
    b = int(input())

    amount = 0
    i = 0
    while i <= b-a+2:
        amount += a
        a += 1
        i += 1
    print(amount)

def Task13():
    a = int(input())
    amount = 0
    if(0 > a or a > 50):
        print('число не має буми в межах a < 0 or a > 50')
    else:
        for i in range(50-a+1):
            amount += math.pow(a,2)
            a += 1
    print(amount)

def Task14():
    N = int(input())
    K = int(input())

    kk = pow(K,5)

    while pow(K,5) > N:
        K -= 1
    print(K)

def Task15():
    n = int(input())
    kn = math.sqrt(n)
    rez = kn - kn%1
    print(rez)

def Task16():
    n = int(input())
    number = 2
    while math.pow(number,2)+1 < n:
        number += 1
    print(math.pow(number,2)+1)

Task1()
Task2()
Task3()
Task4()
Task5()
Task6()
Task7()
Task8()
Task9()
Task10()
Task11()
Task12()
Task13()
Task14()
Task15()
Task16()








