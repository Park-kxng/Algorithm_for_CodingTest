import sys

sys.setrecursionlimit(10000) # 재귀호출의 최대 깊이 설정
input = sys.stdin.readline
n,m = map(int,input().split) # n : 노드 m : 에지
A = [[] for _ in range(n+1)] # 인접 리스트 정의합니다.
visited = [False] *(n+1) # 방문리스트를 정의합니다.
# v : 현재 노드 
def DFS(v):
    visited[v] = True # 방문했으니 True로 변경합니다.
    for i in A[v]: # 현재 노드의 인접 노드에서 반복문을 돕니다
        if not visited[i]: # 만약 인접 노드가 방문하지 않은 노드라면
            DFS(i) # 깊이우선탐색 진행합니다.

for _ in range(m):
    s,e = map (int, input().split())
    A[s].append[e]
    A[e].append[s]

count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS (i)

print(count)
