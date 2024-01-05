import sys

# 1) 변수 초기화 및 N,M을 입력받습니다.
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 2) 누적합 배열 만들기
prefix_sum = [0] # 누적합 담을 리스트
temp = 0

for num in A:
    temp += num
    prefix_sum.append(temp)

#3) M로 나눠서 나오는 나머지의 대한 리스트를 구한다
answer_list = [0 for col in range(M)]
print(prefix_sum)
for i in range(N+1):
    temp = prefix_sum[i]
    print(temp)
    answer_list[int(temp%M)] += 1
    

# 4)나머지 구간 중 같은 나머지를 같는 것 끼리 짝짓는 조합을 구합니다
answer = 0
print(answer_list)
for item in answer_list:
    if item != 0:
        answer += item * (item-1)

    
print(answer_list)
print(answer/2)


