import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    inputNum = int(input())
    a.append((inputNum,i))  

# 버블 정렬
max = 0
a = sorted(a) # inputNum을 기준으로 정렬됨

for i in range(n):
    temp = a[i][1]
    result = a[i][1] - i
    if max < result :
        max = result

print(max+1)