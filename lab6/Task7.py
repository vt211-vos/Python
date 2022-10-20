import csv
myFile = open("studentsRating.txt", "a", encoding="utf8")
with open("marks.lab6.csv", 'rt', encoding="utf8") as freading:
    creading = csv.reader(freading)
    students = [row for row in creading]
for i in students:
    print(i)
arrMark = sorted([*set([i[4].replace(',','.') for i in students])], key=float)
for i in arrMark:
    counter = 0
    for j in students:
        if(i.replace(".",",") == j[4]): counter += 1
    print(f"{i} => {counter}")
    myFile.write(f"Оцінка:{i} => {counter}(кількість студентів)\n")

arrBoolAnswer = [i[7:] for i in students]
print(arrBoolAnswer)
for i in range(len(arrBoolAnswer[0])):
    counter = 0
    for j in arrBoolAnswer:
        if float(j[i].replace(",",".").replace("-", "0")) > 0: counter += 1
    print(f"{i+1} question => {counter} - right({(100/(len(students)/counter)):.2f}%), {len(students)- counter} - wrong")
    myFile.write(f"{i+1} question => {counter} - right({(100/(len(students)/counter)):.2f}%), {len(students)- counter} - wrong\n")
def ConvertMinutes(x):
    x = x.replace(" хв","").replace(" сек", "")
    arr = x.split(" ")
    return (int(arr[0]) * 60 + int(arr[-1]))
arrTimeMark = [[i[0],ConvertMinutes(i[3]),float(i[4].replace(",","."))] for i in students]
arrTimeMark.sort(key= lambda x: x[-1]/x[1], reverse=True)
myFile.write("Top 5 students mark/time\n")
for i in range(5):
    myFile.write(f"{i+1}. {arrTimeMark[i][0]}\n")
myFile.close()


