from collections import deque

n, m = map(int, input().split())
snake = []
for i in range(n):
    snake.append(list(map(int, input().split())))
visited = [ [False]*m for _ in range(n)]

start = [0,0]
end = [n-1, m-1]

dx, dy = [-1,1,0,0], [0,0,-1,1]

answer = 0
def in_range(x,y):
    if 0 <= x < n and 0 <= y < m :
        return True
    else:
        return False
def BFS(snake, visited, curr):
    global  answer
    q = deque()
    q.append(curr)


    while q :
        v = q.popleft()

        x = v[0]
        y = v[1]
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]

            if in_range(x_,y_) and snake[x_][y_] == 1 and not visited[x_][y_]:
                visited[x_][y_] = True
                if visited[end[0]][end[1]] == True:
                    answer = 1
                q.append([x_,y_])


visited[0][0] = True
BFS(snake, visited, start)
print(answer)


