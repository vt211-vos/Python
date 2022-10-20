data = open(r"Numbers.txt", "r").readlines()
amount = 0
for i in range(len(data)):
    data[i] = int(data[i])
    amount += data[i]
print(f"Сума чисел => {amount}")

open("Numbers.txt", "r").close()