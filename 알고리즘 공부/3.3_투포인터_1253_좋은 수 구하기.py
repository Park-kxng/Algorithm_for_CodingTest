import sys

input = sys.stdin.readline
N = int(input()) # 수의 개수
A = list(map(int, input().split())) # 숫자 리스트

# 어떤 수가 다른 수 2개의 합으로 나타낼 수 있으면 좋다라고 함
# 좋은 수는 몇개임?

A.sort()


# 두 재료의 고유한 번호를 합쳐서 M이 되게 하는 경우의 수를 구하여라

count = 0

for k in range(N):
    find = A[k]
    i = 0
    j = N - 1
    while i < j :
        temp = A[i]+A[j]
        if temp == find:
            if i != k and j != k:
                count += 1
                break
            if i == k :
                i += 1
            if j == k :
                j -= 1
        elif temp < find:
            i += 1
        else:
            j -= 1
print(count)
           

     