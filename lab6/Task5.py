import time
import os
path = "guest_book.txt"
print("Введіть 0 для закінчення")
def WriringName():
    value = input("Введіть ім'я ")
    if value != '0':
        print("Hello " + value)
        ModTime = time.ctime(os.path.getmtime(path))
        with open("guest_book.txt", "a", encoding="utf8") as file:
            file.write(f"Hello {value}")
        with open("guest_book.txt", "a", encoding="utf8") as file:
            file.write(f" time: {ModTime}\n")
        WriringName()
result = os.stat("guest_book.txt")
if result.st_size == 0:
    ModTime = time.ctime(os.path.getmtime(path))
    with open("guest_book.txt", "w", encoding="utf8") as file:
        ModTime = time.ctime(os.path.getctime(path))
        file.write(f"Created {ModTime}\n")
WriringName()