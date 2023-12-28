import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))
answer = 0

def binary_search(arr, target):
    global answer
    answer = 0
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            answer = 1 # 찾는 값이 중간 값과 같으면 해당 인덱스 반환
            break
        elif arr[mid] < target:
            left = mid + 1  # 중간 값보다 큰 경우 오른쪽 부분 탐색
        else:
            right = mid - 1  # 중간 값보다 작은 경우 왼쪽 부분 탐색
    print(answer)


for i in B:
  binary_search(A, i)