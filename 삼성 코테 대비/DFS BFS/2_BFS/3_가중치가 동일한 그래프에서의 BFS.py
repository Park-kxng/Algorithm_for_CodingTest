# 가중치가 동일한 그래프에서의 BFS는 최단거리를 구한다
from collections import  deque
n, m = map(int, input().split())
snake = []


for i in range(n):
    snake.append(list(map(int,input().split())))
visited = [[False]* m for _ in range(n)]
# 최단 거리 저장
steps = [[0] * m for _ in range(n)]

answer = 0
start_x , start_y = 0,0
end_x, end_y = n-1, m-1


dxs, dys = [1,-1,0,0], [0,0,1,-1]

def in_range(x,y):
    if 0<= x < n and 0 <= y < m:
        return True
    else:
        return False
def BFS(snake, visited, curr):
    global steps

    q = deque()
    q.append(curr)
    visited[start_x][start_y] = True
    steps[start_x][start_y] = 0


    while q :
        curr_v = q.popleft()
        x = curr_v [0]
        y = curr_v [1]

        for dx, dy in zip(dxs, dys):
            x_ = x + dx
            y_ = y + dy

            if in_range(x_,y_) and not visited[x_][y_] and snake[x_][y_] == 1 :
                visited[x_][y_] = True
                steps[x_][y_] = steps[x][y] + 1
                q.append([x_,y_])




BFS(snake, visited,[start_x, start_y])

# 정답
if steps[end_x][end_y] == 0 :
    print(-1)
else:
    print(steps[end_x][end_y])
