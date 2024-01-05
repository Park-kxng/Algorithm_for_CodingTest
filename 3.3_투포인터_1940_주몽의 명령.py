import sys

input = sys.stdin.readline
N = int(input()) # 재료의 개수
M = int(input()) # 갑옷을 만드는 데 필요한 개수
A = list(map(int, input().split())) # 재료들이 가진 고유한 번호 리스트

# 두 재료의 고유한 번호를 합쳐서 M이 되게 하는 경우의 수를 구하여라
start_index = 1
end_index = 1

count = 0
for item in A:
    temp = M - item
    if temp in A:
        A.remove(temp)
        count += 1

print(count)
 