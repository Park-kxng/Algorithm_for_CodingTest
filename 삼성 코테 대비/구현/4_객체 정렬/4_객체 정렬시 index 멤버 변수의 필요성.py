class student:
    def __init__(self, height, weight, index = 0):
        self.height = int(height)
        self.weight = int(weight)
        self.index = index

n = int(input())
arr = []

for i in range(n):
    height, weight = input().split()
    arr.append(student(height, weight, i+1))

arr_sorted = arr.sort(key=lambda x : (-x.height, -x.weight, x.index))

for a in arr :
    print(a.height, a.weight, a.index)