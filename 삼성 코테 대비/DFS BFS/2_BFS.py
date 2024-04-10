from collections import  deque

# BFS 기본 예제
def BFS(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


graph = [
    [], # 안쓰는 노드
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]

n = len(graph)
visited = [False] * (n+1)
BFS(graph,1,visited)