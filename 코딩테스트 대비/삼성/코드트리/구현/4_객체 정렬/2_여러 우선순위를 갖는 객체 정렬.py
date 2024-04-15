class student:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.mat = int(mat)

n = int(input())
arr = []

for _ in range(n):
    name, kor, eng, mat = input().split()
    arr.append(student(name, kor, eng, mat))

arr.sort(key=lambda x : (-x.kor, -x.eng, -x.mat))

for a in arr :
    print(a.name, a.kor, a.eng, a.mat)