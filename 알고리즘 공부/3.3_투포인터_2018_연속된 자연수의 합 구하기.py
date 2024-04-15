import sys

# 1) 변수 초기화 및 N,M을 입력받습니다.
input = sys.stdin.readline
N = int(input())
start_index = 1
end_index = 1

count = 1
sum = 1
while end_index != N :
    print(end_index)
    if sum == N :
        count += 1
        end_index += 1
        sum += end_index
    
    elif sum > N:
        sum -= start_index
        start_index += 1
    else :
        end_index += 1
        sum += end_index

print(count)
