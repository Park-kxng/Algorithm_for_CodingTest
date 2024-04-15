import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
miro = [[0] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().rstrip()))
    for j in range(m):
        miro[i][j] = temp[j]

def BFS(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        now = q.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0 <= x < n and 0 <= y < m:
                if miro[x][y] == 1 and not visited[x][y]:
                    visited[x][y] = True
                    miro[x][y] = miro[now[0]][now[1]] + 1
                    q.append((x, y))

BFS(0, 0)
print(miro[n - 1][m - 1])
