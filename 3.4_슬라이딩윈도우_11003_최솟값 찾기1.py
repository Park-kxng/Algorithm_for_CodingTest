# import sys

# input = sys.stdin.readline

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# min = A[0]
# second_min = A[1]
# # 최솟값 찾기
# for i in range(2,M):
#     if min > A[i] :
#         min = A[i]
#     elif second_min > A[i] and second_min > min:
#         second_min = A[i]

# print(min, second_min)   
# start = 0
# for i in range(M-1):
#     print(min)
# for i in range(1, N - M + 1): # 슬라이딩 윈도우
#     if start < M -1 :
#         print(min)
#     # 윈도우에서 하나 빼고 새로운 문자 추가
#     out_char = A[i - 1]
#     in_char = A[i + M - 1]
#     # 빼려는 문자가 최솟값이면 두번째로 최소인 아이를 넣는다
#     if out_char == min :
#         min = second_min
#     # 두번째로 작은 숫자를 찾는다.
#     #print(second_min, in_char, min)
#     if A[i] > in_char and in_char > min:
#         second_min = in_char
    

#     # 들어오는 문자는 최솟값과 비교하여 최솟값을 결정한다
#     if in_char < min :
#         min = in_char
    
#     #print(min,second_min)

from collections import deque

N, L = map(int, input().split())
nums = list(map(int, input().split()))
min = nums[0]
second_min = nums[1]
# 최솟값 찾기
for i in range(2,L):
    if min > nums[i] :
        min = nums[i]

for i in range(L-1):
    print(min)

result = []
deq = deque()


for i in range(N):
    # Deque에서 벗어난 값을 제거
    while deq and deq[0] < i - L + 1:
        deq.popleft()

    # Deque의 마지막 값이 현재 값보다 크면 제거 (최솟값 유지)
    while deq and nums[deq[-1]] > nums[i]:
        deq.pop()

    # 현재 인덱스를 Deque에 추가
    deq.append(i)

    # L 길이의 윈도우에 도달하면 결과에 최솟값 추가
    if i >= L - 1:
        print(nums[deq[0]])



