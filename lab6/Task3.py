data = open(r"learning_python.txt", "r", encoding='utf8').readlines()
print(data)
print(sorted(data, key = len, reverse=True))
open("learning_python.txt", "r").close()