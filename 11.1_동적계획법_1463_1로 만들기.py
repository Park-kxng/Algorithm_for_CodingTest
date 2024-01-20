import sys

input = sys.stdin.readline
n = int(input())
D = [ 0 for _ in range(n+1)]

for i in range(2,n+1):
    D[i] = D[i-1]+1
    if i%2 == 0 :
        D[i] = min(D[i], D[i//2]+1)
    if i%3 == 0:
        D[i] = min(D[i], D[i//3]+1)

# 3으로 나누어 떨어지면, 3으로 나눈다.
# 2으로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다

print(D[n])