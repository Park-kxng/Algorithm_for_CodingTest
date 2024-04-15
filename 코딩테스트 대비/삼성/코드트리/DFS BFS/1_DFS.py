# 기본적인 DFS 예제
def DFS(graph,v,visited):
        visited[v] = True
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                DFS(graph,i,visited)

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
DFS(graph,1,visited)
