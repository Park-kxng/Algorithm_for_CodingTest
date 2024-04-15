import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))


prefix_sum = [0] # 누적합 담을 리스트
temp = 0

for num in numbers:
    temp += num
    prefix_sum.append(temp)

for i in range(M):
    start, end = map(int, input().split())
    print(prefix_sum[end]-prefix_sum[start-1])

        




