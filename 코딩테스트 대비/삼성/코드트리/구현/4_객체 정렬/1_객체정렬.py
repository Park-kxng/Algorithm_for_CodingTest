class Student:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

n = int(input())
arr = []
for _ in range(5):
    name, height, weight = input().split()
    arr.append(Student(name,height,weight))

arr.sort(key=lambda x : x.h)
for a in arr :
    print(a.n, a.h, a.w)