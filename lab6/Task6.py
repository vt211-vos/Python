import os
import time
import re
if not os.path.exists("WordsAboutPython.txt"):
    myFile = open("WordsAboutPython.txt", 'w', encoding="utf8")
    ModTime = time.ctime(os.path.getctime("WordsAboutPython.txt"))
    myFile.write(f"Created {ModTime}\n")
    myFile.close()


with open("AboutPython.txt", 'r', encoding="utf8") as myFile2:
    data = myFile2.read()

data = re.sub("[,.-]", "", data)
data = data.lower()
arr = [*set(data.split(" "))]
print(arr)
for i in arr:
    t1 = time.perf_counter()
    number = data.count(i)
    t2 = time.perf_counter()
    with open("WordsAboutPython.txt", 'a', encoding='utf8') as myFile:
        myFile.write(f"{i} => {number}  time => {(t2-t1):.6f}\n")



