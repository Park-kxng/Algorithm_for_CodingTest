n,m = map(int,input().split())
graph = [[0] * (n+1) for i in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    x, y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

answer = []
def DFS(graph,visited, v):
    global  n
    global answer
    for curr_v in range(1,n+1):
        # print(v, curr_v, graph[v][curr_v])
        if graph[v][curr_v] == 1 and not visited[curr_v]:
            answer.append(curr_v)
            visited[curr_v] = True
            DFS(graph, visited, curr_v)

visited[1] = True
DFS(graph, visited, 1)
print(len(answer))