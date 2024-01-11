import sys
from collections import deque
input = sys.stdin.readline



# n : 정점의 개수
# m : 간선의 개수
# v(start) : 탐색을 시작한 정점의 번호
n, m, start = map(int, input().split())
ad_list = [[] for i in range(n+1)] # 인접 리스트

# 정점 번호는 1-N
# 그래프 저장하기
for i in range(1,m+1):
    a, b = map(int, input().split())
    ad_list[a].append(b)
    ad_list[b].append(a)

# 방문할 수 있는 정점 여러개 - 번호가 작은 것 먼저
for i in range(n+1):
    ad_list[i].sort() # 오름차순 (작은 거 먼저)

def DFS(v):
    print(v, end='')
    visited[v] = True
    for i in ad_list[v]:
        if not visited[i]:
            DFS(i)


def BFS(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now_node = q.popleft()
        print(now_node, end= ' ')
        for i in ad_list[now_node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

visited = [False] * (n+1)
DFS(start)
print()
visited = [False] * (n+1)
BFS(start)

# DFS와 BFS 로 탐색한 결과를 출력
