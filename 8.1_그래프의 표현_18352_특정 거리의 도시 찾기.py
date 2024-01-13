import sys
from collections import deque
input = sys.stdin.readline
# 도시의 개수 n
# 도로의 개수 m
# 거리 정보 k
# 출발 도시 x
n, m , k, x = map(int, input().split())
node = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
q = deque()
for i in range(m):
    a, b = map(int, input().split()) # 단방향 a->b
    node[a].append(b)
# x로부터 출발해 도달 가능한 도시 중 최단 거리가 k인 모든 도시의 번호 (오름차순 출력)
    
depth = 0

# BFS 탐색
def BFS(v):
    global depth
    q = deque()
    q.append(v)
    visited[v] = depth
    depth += 1
    while q:
        now_node = q.popleft()
        for i in node[now_node]:
            
            if visited[i] == -1:
                visited[i] = depth
                q.append(i)
        depth += 1        

answer = []
BFS(x)

for i in range(1,n+1):
    temp = visited[i]
    if temp == k:
        answer.append(i)

answer.sort()
if len(answer) == 0:
    print(-1)
else:
    for an in answer:
        print(an)