n,m = map(int,input().split(' '))
arr = [[0]* m for _ in range(n)]
curr = [0,0]
dx ,dy = [0,1,0,-1],[1,0,-1,0]
curr_d = 0
count = 1
def in_range(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

for i in range(0,n*m):
    x,y = curr[0], curr[1]
    arr[x][y] = count

    x_ = x + dx[curr_d]
    y_ = y + dy[curr_d]

    if not in_range(x_,y_) or arr[x_][y_] != 0:
        curr_d = (curr_d + 1) % 4
        x_ = x + dx[curr_d]
        y_ = y + dy[curr_d]

    count += 1
    curr = [x_, y_]

arr[0][0] = 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()

