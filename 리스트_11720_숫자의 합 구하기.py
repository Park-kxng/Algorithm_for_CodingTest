import sys

input = sys.stdin.readline
N = int(input())
A = list(input())

print(A)

sum = 0
for i in range(N):
    sum += int(A[i])

print(sum)