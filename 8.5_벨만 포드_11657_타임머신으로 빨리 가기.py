import sys
from queue import PriorityQueue
# 입력 받기
input = sys.stdin.readline
n,m = map(int, input().split())
bus = [[] for _ in range(n+1)]
visited = [ False for _ in range(n+1)]
q = PriorityQueue()

distance = [sys.maxsize for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    bus[a].append((b,c))
print(bus)
    
    

q.put((0,1)) # k를 시작점으로 설정 (우선순위, 버스 번호)
distance[1] = 0


# while q.qsize() > 0:
#     cur = q.get()
#     cur_v = cur[1]
#     if visited[cur_v]:
#         continue
#     visited[cur_v] = True
#     for tmp in ad[cur_v]:
#         next = tmp[0] # 노드
#         value = tmp[1] #가중치
#         if min_distance[next] > min_distance[cur_v] + value:
#             min_distance[next] = min_distance[cur_v] + value
#             q.put((min_distance[next],next))
        

    
# # 최단경로값 출력 (시작점은 0, 경로가 없을 때에는 INF를 출력)
    
# for i in range(1,len(min_distance)):

#     if visited[i]:
#         print(min_distance[i])

#     else:
#         print('INF')



