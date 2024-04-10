# N*M 크기의 얼음틀

# DFS
def DFS(arr,i,j,visited,n,m):
    move_type = [[0,1],[0,-1],[1,0],[-1,0]]
    visited[i][j] = True
    check_lst = []
    for move in move_type:
        i_ = i + move[0]
        j_ = j + move[1]

        if 0<=i_<n and 0<= j_ <m and arr[i_][j_] == 0 and not visited[i_][j_] : #범위 안에 있으면
            check_lst.append([i_,j_])


    for check in check_lst:
        i = check[0]
        j = check[1]
        if not visited[i][j]:
            DFS(arr, i,j ,visited,n,m)
# 초기화
n,m = map(int,input().split())
visited = [[False] * m for _ in range(n)]
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 :
            visited[i][j] = True

answer = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            # 깊이 실행 DFS()

            DFS(arr, i, j, visited,n,m)
            answer += 1
print(answer)
