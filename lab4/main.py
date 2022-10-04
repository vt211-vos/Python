import math
import random
'''/////////// 1 ///////////'''
# list = []
# print("Введіть кількість елементів у масиві")
# n = int(input())
# for i in range(n):
#     list.append(int(input()))
#
# print(f"Max => {max(list)}")
# print("Reverse")
# list.reverse()
# print(list)

'''/////////// 2 ///////////'''
# list = []
# print("Введіть кількість елементів у масиві")
# n = int(input())
# for i in range(n):
#     print(f"{i + 1}:")
#     list.append(int(input()))
#
# list2 = []
# list3 = []
# for i in list:
#     if i > 0:
#         list2.append(i)
#     else:
#         list3.append(i)
#
# print(list2)
# print(list3)

'''/////////// 3 ///////////'''
# list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2]
# amount = 0
# for i in range(len(list)):
#     if i % 2 == 1:
#         amount += list[i]
#
# print(f"Сума чисел з непраним індексом = {amount}")
# print(list)

'''/////////// 4 ///////////'''
# list = []
#
# for i in range(30):
#     r = random.randrange(-100,100)
#     list.append(r)
#
# max_value = max(list)
# max_index = list.index(max_value)
# print(f"Max value => {max_value}, index of max => {max_index}")
#
# list2 = []
#
# for i in list:
#     if i % 2 == 1:
#         list2.append(i)
# if len(list2) != 0:
#     list2.sort()
#     list2.reverse()
#     print(list2)
# else:
#     print("Нема непарних")

'''/////////// 5 ///////////'''
# list = []
#
# for i in range(30):
#     r = random.randrange(-100,100)
#     list.append(r)
#
# for i in range(len(list) - 1):
#     if list[i] < 0 and list[i + 1] < 0:
#         print(f"({list[i]}, {list[i + 1]})")

'''/////////// 6 ///////////'''
# list = []
# list2 = []
#
# for i in range(10):
#     r = random.randrange(-100,100)
#     list.append(r)
# print('max - list[i]')
# max_value = max(list)
# for i in list:
#     if i < max_value:
#         print(f"{max_value} - {i} = {max_value - i}")
#         list2.append(int(math.pow(i,2)))
# list2.sort()
# list2.reverse()
# print(list2)

'''/////////// 7 ///////////'''
# list = []
#
# for i in range(30):
#     r = round(random.uniform(-100.0,100.0),2)
#     list.append(r)
# myMin = math.fabs(list[0])
# for i in range(len(list)):
#     if myMin > math.fabs(list[i]):
#         myMin = math.fabs(list[i])
# print(f'Найменше по модулю => {myMin}')
# list.sort()
# print(list)

'''/////////// 8 ///////////'''
# list = []
# list2 = [[],[],[],[],[],[],[],[],[],[]]
# j = 0
#
# for i in range(0,30):
#     if i % 3 == 0 and i != 0:
#         j += 1
#     r = round(random.uniform(-100.0, 100.0), 2)
#     list2[j].append(r)
#
# print(list2)
# for j in range(len(list2)-1):
#     for i in range(len(list2)-1):
#         x1  = math.fabs(list2[i][0])+ math.fabs(list2[i][1]) + math.fabs(list2[i][2])
#         x2 = math.fabs(list2[i + 1][0]) + math.fabs(list2[i + 1][1]) + math.fabs(list2[i + 1][2])
#         if x1 > x2:
#             temp = list2[i]
#             list2[i] = list2[i + 1]
#             list2[i + 1] = temp
#
# for i in list2:
#     print(i)

