import sys
from collections import deque

input = sys.stdin.readline

# 1) 입력
n = int(input()) # 입력할 줄 개수 및 건물의 종류 수 

d = [0 for _ in range(n)]  # 진입 차수 리스트
times = [0 for _ in range(n)] #빌딩 짓는 시간 담는 리스트
answer = [0 for _ in range(n)] # 정답 리스트
node = [[] for _ in range(n)]
q = deque() # 위상정렬리스트

for j in range(n):
    temp = list(input().split())
    size = len(temp)
    # 빌딩 짓는 시간 넣기
    time = int(temp[0])
    times[j] = time
    # 진입 차수 리스트 넣기
    for i in range(1,size):
        cur_num = int(temp[i])
        if cur_num != -1:
            node[cur_num-1].append(j+1)

            d[j] += 1
      
# 2) 위상 정렬로 건물 줄 세우기
for i in range(1, n+1):
    if d[i-1] == 0:
        q.append(i)

result = []

while q:
    cur_building = q.popleft()

    for next_building in node[cur_building-1]:
        d[next_building-1] -= 1
        answer[next_building-1] = max(answer[next_building-1],answer[cur_building-1]+times[cur_building-1])
        if d[next_building-1] == 0:
            q.append(next_building)

# 3) 출력: 건물 순서대로 걸리는 시간 출력하기

for i in range(n):
    temp = times [i]+ answer[i]
    print(temp)

