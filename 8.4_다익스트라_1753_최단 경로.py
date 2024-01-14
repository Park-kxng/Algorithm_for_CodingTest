import sys
from queue import PriorityQueue
# 입력 받기
input = sys.stdin.readline
v,e = map(int,input().split())
k = int(input()) # 시작점
ad = [[]for _ in range(v+1)]
visited = [ False for _ in range(v+1)]
min_distance = [sys.maxsize for _ in range(v+1)]
q = PriorityQueue()

for i in range(e):
    u,v_, w_ = map(int, input().split())
    ad[u].append((v_,w_)) # u->v (가중치 w)

q.put((0,k)) # k를 시작점으로 설정
min_distance[k] = 0


while q.qsize() > 0:
    cur = q.get()
    cur_v = cur[1]
    if visited[cur_v]:
        continue
    visited[cur_v] = True
    for tmp in ad[cur_v]:
        next = tmp[0] # 노드
        value = tmp[1] #가중치
        if min_distance[next] > min_distance[cur_v] + value:
            min_distance[next] = min_distance[cur_v] + value
            q.put((min_distance[next],next))
        

    
# 최단경로값 출력 (시작점은 0, 경로가 없을 때에는 INF를 출력)
    
for i in range(1,len(min_distance)):

    if visited[i]:
        print(min_distance[i])

    else:
        print('INF')



