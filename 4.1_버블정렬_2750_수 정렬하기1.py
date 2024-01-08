import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    inputNum = int(input())
    a.append(inputNum)

# 버블 정렬
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

for ans in a:
    print(ans)

