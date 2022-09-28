# str = ("If you can keep your head when all about you "
#        "Are losing theirs and blaming: it on you, "
#        "If you can trust yourself when all men doubt you, "
#        "But make allowance for their doubting too; "
#        "If you can wait: and not be tired by waiting, "
#        "Or being lied about, don't deal in lies, "
#        "Or being: hated, don't give way to hating, "
#        "And yet don't look too good,: nor talk too wise: ")
# print('Завдання 1. Дано рядок, що містить текст \n'+
#       '(до тисячі слів). Знайти кількість слів,\n'+
# 'що починаються з заданої користувачем літери без \nврахування регістру.')
# print('Введіти літеру:')
# a = input()
# print(f"Знайдена кількість: {str.count(' ' + a.upper()) + str.count(' ' + a.lower())}")

"""////////////////////////2/////////////////////////////"""
# str2 = "В текс:ті з:аміни:ти в:сі: двокрапки :(:) : знаком відсотка (%)"
# print('В тексті замінити: всі двокрапки (:) знаком відсотка (%).'+
#        'Підрахувати кількість замін')
# j = 0
# print(str2)
# for i in str2:
#     if i == ':':
#         str2 = str2.replace(i, '%')
#         j+=1
# print(str2)
# print(f'Кількість замін: {j}')

''''///////////////////////3/////////////////////////////'''
# print('Завдання 3. В тексті видалити символ крапки '+
#       '(.) І підрахувати кількість віддалених символів.')
# str = ". В т.ексті. вид.алити .сим.в.ол крап.ки (.)"
# print(str)
# j = 0
# for i in str:
#     if i == '.':
#         str = str.replace(i, '')
#         j+=1
# print(str)
# print(f'Кількість видалень: {j}')

'''////////////////////////4/////////////////////////////'''
# print("Завдання 4. В тексті замінити букву (а)\n"+
#       " буквою (о). Підрахувати кількість замін.\n"+
#       "Підрахувати, скільки символів в рядку.")
# str = "В тексті заміанаити букву (аа) букваою (о)"
# print(str)
# j = 0
# for i in str:
#     if i == 'а':
#         str = str.replace(i, 'о')
#         j+=1
# print(str)
# print(f'Кількість замін: {j}')

'''////////////////////////5/////////////////////////////'''
# print("Завдання 5. У рядку замінити всі великі літери малими.")
# str = "У РядКу зАмінитИ вСі великІ ЛІтеРи малими"
# print(str)
# print(str.lower())

'''////////////////////////6/////////////////////////////'''
# print('Завдання 6. В рядку видалити літери '+
#       '"o" І підрахувати кількість віддалених символів.')
# str = "В тоекстоі видоалити ліотирои 'о'"
# print(str)
# j = 0
# for i in str:
#     if i == 'о':
#         str = str.replace(i, '')
#         j+=1
# print(str)
# print(f'Кількість видалень: {j}')

'''////////////////////////7/////////////////////////////'''
# print('Завдання 7. Дано рядок. Перетворити його,'+
#       ' замінивши зірочками всі букви "п", що'+
#       ' зустрічаються серед перших n / 2 символів. Тут n - довжина рядка.')
# str = "Пішов пастернак пити пиво пішки по дорозі"
# print(str)
# x = int(len(str)/2)
# str = str.replace(str[0:x], str[0:x].replace('п','*'))
#
# print(str)

'''//////////////////////////8///////////////////////////'''
# print('Визначити, скільки разів в тексті зустрічається задане слово.')
# str = 'Lorem sed ipsum dolor sed sit amet, consectetur adipiscing elit,'+\
#       ' sed do eiusmod tempor dolor incididunt ut labore et dolore magna aliqua'
# print(str)
# print('Введіти слово:')
# a = input()
# print(f"Знайдена кількість: {str.count(' ' + a + ' ')}")

'''//////////////////////////9///////////////////////////'''
# print('Дано рядок на англійській мові, що містить текст (до тисячі слів).'+
#       'Перетворити рядок так, щоб кожне слово починалося з великої літери.')
# str = 'Lorem sed ipsum dolor sed sit amet, consectetur adipiscing elit,'+\
#       ' sed do eiusmod tempor dolor incididunt ut labore et dolore magna aliqua'
# print(str)
# print(str.title())

'''//////////////////////////10//////////////////////////'''
# print("Завдання 10. Дано рядок на англійській мові, що містить "+
#       "текст (до тисячі слів)."+
#       "Вивести всі слова, що починаються на літеру N"+
#       " і слова що закінчуються налітеру P. Літери "+
#       "N і P вводяться користувачем")
# str = 'Lorem sed ipsum dolor sed sit amet, consectetur adipiscing elit,'+\
#       ' sed do eiusmod tempor dolor incididunt ut labore et dolore magna aliqua'
# print(str)
# str = str.replace(",", "")
# str = str.replace(":", "")
# str2 = str.split()
# print("Введіть N")
# n = input()
# print("Введіть P")
# p = input()
# for i in  str2:
#       if i[0] == n:
#             print(i)
#       elif i[-1] == p:
#             if i[0] != n:
#                   print(i)

'''//////////////////////////11//////////////////////////'''
# str = 'Lorem sed ipsum dolor sed sit amet, consectetur adipiscing elit,'
# print(str)
# str = str.lower()
# a = ['e','y','u','i','o','a'];
#
# amount = 0
# for i in a:
#       amount += str.count(i)
# print(amount)

'''//////////////////////////12//////////////////////////'''
# str = 'Lorem sed ipsum dolor sed sit amet, consectetur adipiscing elit,'
# print(str)
# str = str.lower()
# a = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'];
#
# amount = 0
# for i in a:
#       amount += str.count(i)
# print(amount)

'''//////////////////////////13//////////////////////////'''
str = 'Lorem Sed ipsum Dolor sed sit Amet, consectetur adipiscing elit,'
print(str)

str2 = str.split()
amount = 0
for i in range(1,len(str2)-1):
      if str2[i][0].isupper():
            print(str2[i])