import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
answer = 0

# 삽입정렬
for i in range(1,len(a)):
    inserted_point = i
    inserted_value = a[i]
    for j in range(i-1,-1,-1):
        # 자기 자리 찾아서 넣기
        if a[j] < a[i]: # 넣을 자리 찾으면 저장하고 break
            inserted_point = j+1
            break
        if j == 0: # 끝까지 못 찾으면 0
            inserted_point = 0
    for j in range(i,inserted_point,-1):
        a[j] = a[j-1] # 뒤로 밀고
    a[inserted_point] = inserted_value # 넣을 자리에 넣기



# 누적합
prefix_sum = [0] # 누적합 담을 리스트
temp = 0

for num in a:
    temp += num
    prefix_sum.append(temp)   

# 누적합의 전체 합을 구한다
print(sum(prefix_sum))
