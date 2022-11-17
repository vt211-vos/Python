import csv
import matplotlib.pyplot as plt
import os

class KmrCsv:
    def __init__(self, ref = "marks2.lab11.csv", num = 2):
        self.ref = ref
        self.num = num
class Statistic:
    def __init__(self, ref ="marks2.lab11.csv" ):
        with open("marks2.lab11.csv", 'rt', encoding="utf8") as freading:
            creading = csv.reader(freading)
            students = [row for row in creading]
            self.students = students
    def avg_stat(self):
        with open("marks2.lab11.csv", 'rt', encoding="utf8") as freading:
            creading = csv.reader(freading)
            students = [row for row in creading]
            self.students = students
        arrBoolAnswer = [i[7:] for i in self.students]
        arr =[]
        for i in range(len(arrBoolAnswer[0])):
            counter = 0
            for j in arrBoolAnswer:
                if float(j[i].replace(",", ".").replace("-", "0")) > 0: counter += 1
            arr.append([i, (100 / (len(self.students) / counter))])
        return arr

    def marks_stat(self):
        with open("marks2.lab11.csv", 'rt', encoding="utf8") as freading:
            creading = csv.reader(freading)
            students = [row for row in creading]
            self.students = students

        arr =[]
        arrMark = sorted([*set([i[4].replace(',', '.') for i in self.students])], key=float)
        for i in arrMark:
            counter = 0
            for j in self.students:
                if (i.replace(".", ",") == j[4]): counter += 1
            arr.append([i, counter])
        return arr

    def marks_per_time(self):
        def ConvertMinutes(time, mark):
            time = time.replace(" хв", "").replace(" сек", "")
            arr = time.split(" ")
            return (mark / int(arr[0]))

        arrTimeMark = [[i[0], ConvertMinutes(i[3], float(i[4].replace(",", ".")))] for i in self.students]
        return arrTimeMark

    def best_marks_per_time(self, bottom_margin, top_margin):
        arr = []
        def ConvertMinutes(time, mark):
            time = time.replace(" хв", "").replace(" сек", "")
            arr = time.split(" ")
            return (mark / int(arr[0]))

        arrTimeMark = [[i[0], ConvertMinutes(i[3], float(i[4].replace(",", "."))), float(i[4].replace(",", "."))] for i in self.students]
        arrTimeMark.sort(key=lambda x: x[1], reverse=True)
        print("Top 5 students mark/time\n")
        counter = 0
        for i in arrTimeMark:
            if i[2] > bottom_margin and i[2] < top_margin and counter < 5:
                arr.append(i)
                counter += 1
        return arr
class Plots:
    def set_cat(self, name):
        os.mkdir(name)
    def avg_plot(self, arr):
        arr1 = [i[0] for i in arr]
        arr2 = [i[1] for i in arr]
        plt.plot(arr1, arr2)
        plt.show()
        plt.savefig(f'diagrams\\foo.png')
    def marks_plot(self, arr):
        arr1 = [i[0] for i in arr]
        arr2 = [i[1] for i in arr]
        plt.plot(arr1, arr2)
        plt.show()
        plt.savefig(f'diagrams\\2.png')
class KmrWork(KmrCsv, Statistic, Plots):
    kmrs = "marks2.lab11.csv"
    cat = "diagrams"
    def __init__(self):
        self.path = "marks2.lab11.csv"


s = Statistic()
arr = s.avg_stat()
print(arr)


mk = KmrWork()
mk.avg_plot(mk.avg_stat())
mk.marks_plot(mk.marks_stat())
