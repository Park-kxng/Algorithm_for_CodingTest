# 두 방향 탈출 가능 여부 판별하기
# 입력값 받기
n, m = map(int, input().split())

snake = [] # 뱀이 없으면 1 있으면 0
for i in range(n):
    snake.append(list(map(int, input().split())))
# 방문 여부 저장
visited = [[0]*m for _ in range(n)]

# 처음과 끝 x,y값 저장
start = [0,0]
end = [n-1, m-1]
# 정답 (탈출 여부)
answer = 0

dx, dy = [1,0],[0,1]
def in_range(x,y):
    if 0<= x < n and 0 <= y < m :
        return True
    else:
        return False
def DFS(snake, visited, curr):
    global  answer
    x ,y = curr[0], curr[1]
    temp_x , temp_y = 0, 0

    for i in range(2):
        temp_x = x + dx[i]
        temp_y = y + dy[i]

        # 격자 안에 있는지, 뱀이 없는지, 방문한 적 있는지
        if in_range(temp_x, temp_y) and snake[temp_x][temp_y] == 1 and not visited[temp_x][temp_y] :
            visited[temp_x][temp_y] = True
            if temp_x == end[0] and temp_y == end[1] :
                answer = 1
            DFS(snake, visited, [temp_x,temp_y])



visited[start[0]][start[1]] = 0
DFS(snake, visited, start)
print(answer)
