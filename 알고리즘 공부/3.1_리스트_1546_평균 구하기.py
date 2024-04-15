import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
M = max(A)
for i in A:
    print(i)
    i = (i/M) * 100
    print(i)

print(M, A)

