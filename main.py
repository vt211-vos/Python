import math
import random
import time

def Area(a,b):
    return a * b;
def Task1():
    for i in range(3):
        print(f"Сторони пряиокутника №{i + 1}")
        print("Введіть а:")
        a = float(input())
        print("Введіть b:")
        b = float(input())
        print(Area(a, b))


def Hypotenuse(a,b):
    return math.sqrt(a**2 + b**2)
def Task2():
    list = []
    for i in range(2):
        print(f"Катети трикітника №{i + 1}")
        print("Введіть а:")
        a = float(input())
        print("Введіть b:")
        b = float(input())
        list.append(Hypotenuse(a, b))
    if list[0] > list[1]:
        print("Гіпотенуза першого більша")
    else:
        print("Гіпотенуза другого більша")


def circleIncludes(a, b, r):
    def Point(x, y):
        if (x - a) ** 2 + (y - b) ** 2 < r ** 2:
            print("Точка входить в коло")
        else:
            print('Точка не входить в коло')

    for i in range(3):
        print(f"Точка {i+ 1}")
        print("x:")
        x = int(input())
        print("y:")
        y = int(input())
        Point(x, y)
def Task3():
    print("Введіть інфо про коло R, X, Y")
    print("X:")
    x = int(input())
    print("Y:")
    y = int(input())
    print("R:")
    r = int(input())
    circleIncludes(x,y,r)


def AreaFour(x,y,z,t):
    Area1 = x * y
    hypoten = Hypotenuse(x,y)
    p = (hypoten + z + t)/2
    Area2 = math.sqrt(p*(p-hypoten)*(p-z)*(p-t))
    S = Area1 + Area2;
    print(round(S, 3))
def Task4():
    print("Введіть X:")
    x = float(input())
    print("Введіть Y:")
    y = float(input())
    print("Введіть Z:")
    z = float(input())
    print("Введіть T:")
    t = float(input())
    AreaFour(x,y,z,t)

def Numbers(n, list):
    for i in range(1,n + 1):
        count = 0
        for j in list:
            if j % i == 0:
                count += 1
        if count == len(list):
            print(i)
list = [3,6,9]
#Numbers(7, list)

def MostВivider(m,n):
    list = []
    for i in range(m,n+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
        list.append(count)
    maxValue = list.index(max(list)) + m
    print(maxValue)
def Task6():
    print('M:')
    m = int(input())
    print('N:')
    n = int(input())
    MostВivider(m,n)

def SimpleNumbers(n, v):
    list = []
    for i in range(1,n + 1):
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count == 1:
            list.append(i)
    if v == 1:
        print(list)
    elif v == 2:
        for i in list:
            print(i)
    else:
        len(list)
def Task7():
    n = int(input("Введіть N:"))
    print("Оберіть форму представлення ( 1 -списком;2 - рядками\n в стовпчик;3 - просто вивести кількість простих чисел:")
    v = int(input())
    SimpleNumbers(n,v)

def read_int(text="Введіть число: "):
    try:
        value = int(input(text))
    except Exception:
        print("Не ціле число")
        return read_int(text)
    else:
        return value
def Check(min, max):
    x = read_int()
    if x > max or x < min:
        print("Вийло за межі")
        Check(min, max)
    else: return x

def Task8():
    list = []
    x = random.randint(0,100)
    for i in range(1, x):
        list.append(random.randint(0,100))
    maxValue = max(list)
    minValue = min(list)
    upper = Check(minValue, maxValue)
    bottom = Check(minValue, maxValue)
    NewMax = maxValue - upper
    NewMin = minValue + bottom
    newList = []
    for i in list:
        if i > NewMin and i < NewMax:
            newList.append(i)
    print("Початковий масив")
    print(list)
    print("Новий масив")
    print(newList)

def TimeOperation(func):
    def wrapper():
        t1 = time.perf_counter()
        func()
        t2 = time.perf_counter()
        print(f"Часв виконання: {(t2-t1):.6f}")
    return wrapper

@TimeOperation
def Number10TK6():
    MostВivider(1,10000)

@TimeOperation
def Number10TK7():
    SimpleNumbers(10000,3)

@TimeOperation
def Number10TK8():
    Task8()

Number10TK6()
Number10TK7()
Number10TK8()







