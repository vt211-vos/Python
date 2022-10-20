import  os
with open("learning_python.txt", "r",  encoding="utf8") as file:
    data = file.readlines()

leng = input("Введіть мову програмування ")
dir = "LengProg"
for i in range(len(data)):
    data[i] = data[i].replace("Python", leng)

if not os.path.isdir(dir):
    os.mkdir(dir)

list = []
print(data)
for i in range(len(data)):
    x = int(input("Введіть номер хибного твердження: "))
    if x != 0: list.append(x - 1)
    else: break

file1 = open(f"{dir}\learning_python.txt", "a", encoding="utf8")
file2 = open(f"{dir}\learning_python(wrong).txt", "a", encoding="utf8")
for i in range(len(data)):
      if i in list: file2.write(data[i])
      else: file1.write(data[i])



