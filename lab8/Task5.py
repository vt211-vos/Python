class Buffer:
    def __init__(self):
        self.arr = []
        self.last = 0
        self.arrSum = []
    def add(self, *a):
        i = 0
        self.arrSum.clear()
        arr = self.arr[self.last:len(self.arr)]
        arr.extend(a)
        while i <= len(arr):
            if i+4 < len(arr):
                self.Summ(arr[i:i+5])
                self.arr[len(self.arr):] = arr[i:i+5]
                i += 5
            else:
                self.last = len(self.arr)
                self.arr[len(self.arr):] = arr[i:]
                break
    def Summ(self, a):
        sum = 0
        for i in a:
            sum += i
        print(f"sum => {sum}")
        self.arrSum.append(sum)
    def get_current_part(self):
        return self.arrSum

myByffer = Buffer()
myByffer.add(1,2,3,4,5,6,7,8,9)
print(myByffer.get_current_part())
myByffer.add(1,2,3,4,5,6,7,8,9)
print(myByffer.get_current_part())
myByffer.add(1,2,3,4,5,6,7,8,9,1,22,1,2,3,4)
print(myByffer.get_current_part())


