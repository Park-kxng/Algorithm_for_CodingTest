class student:
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = int(s1)
        self.s2 = int(s2)
        self.s3 = int(s3)

n = int(input())
arr = []
for _ in range(n):
    name, s1, s2, s3 = input().split()
    arr.append(student(name, s1, s2, s3))

arr.sort(key = lambda  x : (x.s1+x.s2+ x.s3))
for a in arr:
    print(a.name, a.s1, a.s2, a.s3)
