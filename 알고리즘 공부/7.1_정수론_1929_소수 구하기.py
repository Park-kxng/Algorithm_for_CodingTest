import sys

input = sys.stdin.readline
m, n = map(int, input().split())
a = []
# m 이상 n 사이의 숫자 중에서 소수를 모두 출력하여라

for i in range(0,n+1):
    a.append(i)

for i in range(len(a)):
    if i == 0 or i == 1 :
        continue
    else:
        for j in range(2*i,len(a)+1,i):
            a[j] = 0

# 답 출력
for i in range(m,n+1):
    if a[i] == 0:
        continue
    else:
        print(a[i])
        