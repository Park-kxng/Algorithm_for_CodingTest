
from collections import deque
# 초기화
n,m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input())))

# BFS (시작지점에서 가까운 노드부터 탐색하기 때문에)
def BFS(i, j):

    q = deque()
    q.append([i,j])

    while q:
        v = q.popleft()
        move_type = [[1,0],[-1,0],[0,1],[0,-1]]
        for move in move_type:
            i_ = v[0] + move[0]
            j_ = v[1] + move[1]
            if 0 <= i_ <n and 0 <= j_ < m and arr[i_][j_] == 1:
                q.append([i_,j_])
                arr[i_][j_] = arr[v[0]][v[1]] + 1
    return arr[n-1][m-1]

answer = BFS(0,0)
print(answer)