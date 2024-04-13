class user:
    def __init__(self, name, score):
        self.n = name
        self.s = score
arr = []
temp = 0
for i in range(0,5):
    name , score = input().split()
    arr.append(user(name, score))
    print(arr[i].s, arr[temp].s)
    if arr[i].s > arr[temp].s :
        temp = i
    print(temp)

print(arr[temp].n, arr[temp].s)