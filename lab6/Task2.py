def TryNumbers():
    try:
        value = float(input("Введіть число: "))
    except Exception:
        print("Не число.Кінець")
    else:
        with open("Task2TXT.txt", 'a', encoding='utf8') as file:
            file.write(f"{str(value)} - {'Парне' if value % 2 ==0 else 'Не парне'}\n")
        TryNumbers()
print("Цикил праює поки ви вводите числа")
TryNumbers()

