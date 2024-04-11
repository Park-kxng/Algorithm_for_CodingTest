n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

# 방문 처리를 위한 3차원 배열: visited[x][y][state] - state: 0(가로), 1(세로), 2(대각선)
visited = [[[False] * 3 for _ in range(n)] for _ in range(n)]
answer = 0

# dx, dy: 상태에 따른 이동 방향 - 가로, 세로, 대각선
dx = [0, 1, 1]
dy = [1, 0, 1]


# 이동 가능한지 체크하는 함수
def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n and house[x][y] == 0


# DFS 탐색 함수
def DFS(x, y, state):
    global answer
    if x == n - 1 and y == n - 1:  # 목표 지점에 도달한 경우
        answer += 1
        return

    # 이동 방향 체크: 가로 -> 가로, 대각선 / 세로 -> 세로, 대각선 / 대각선 -> 가로, 세로, 대각선
    for i in range(3):
        if (state == 0 and i == 1) or (state == 1 and i == 0):  # 가로 <-> 세로 이동 불가
            continue
        nx, ny = x + dx[i], y + dy[i]
        if not is_valid(nx, ny):  # 이동할 칸이 유효하지 않으면 스킵
            continue
        if i == 2 and (not is_valid(x, y + 1) or not is_valid(x + 1, y)):  # 대각선 이동 시, 추가 체크
            continue
        DFS(nx, ny, i)


# 초기 상태에서 DFS 시작 - 처음 파이프는 가로 방향으로 놓여 있음
DFS(0, 1, 0)