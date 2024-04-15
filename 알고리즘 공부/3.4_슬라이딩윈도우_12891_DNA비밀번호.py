import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(input().strip())  # 개행 문자 제거
num_A, num_C, num_G, num_T = map(int, input().split())

count_list = ['A', 'C', 'G', 'T']
lst_M = [0 for _ in range(M)]

# 초기 M개의 문자에 대한 개수 계산
count_A = A[:M].count('A')
count_C = A[:M].count('C')
count_G = A[:M].count('G')
count_T = A[:M].count('T')

# 초기 M개의 문자열이 조건을 만족하는지 확인하고 카운트
if count_A >= num_A and count_C >= num_C and count_G >= num_G and count_T >= num_T:
    count = 1
else:
    count = 0

# 슬라이딩 윈도우로 문자열 탐색
for i in range(1, N - M + 1):
    # 윈도우에서 하나 빼고 새로운 문자 추가
    out_char = A[i - 1]
    in_char = A[i + M - 1]

    # 문자열에서 빠진 문자의 개수 차감
    if out_char == 'A':
        count_A -= 1
    elif out_char == 'C':
        count_C -= 1
    elif out_char == 'G':
        count_G -= 1
    elif out_char == 'T':
        count_T -= 1

    # 새로 들어온 문자의 개수 추가
    if in_char == 'A':
        count_A += 1
    elif in_char == 'C':
        count_C += 1
    elif in_char == 'G':
        count_G += 1
    elif in_char == 'T':
        count_T += 1

    # 조건을 만족하는지 확인하고 카운트
    if count_A >= num_A and count_C >= num_C and count_G >= num_G and count_T >= num_T:
        count += 1

print(count)
