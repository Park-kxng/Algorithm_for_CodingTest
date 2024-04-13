n,r,c = map(int, input().split())
arr = []
d = [[0]*n for _ in range(n)]
x ,y = r-1, c-1
dx, dy = [-1,1,0,0], [0,0,-1,1]
for i in range(n):
    arr.append(list(map(int, input().split())))
answer = []
def in_range(x,y):
    if 0<= x < n and 0<= y < n :
        return True
    else:
        return False

while True:
    curr = arr[x][y]
    answer.append(curr)
    d[x][y] = 1 # 이미 지나간 자리 표시

    for i in range(0,4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        
        if in_range(temp_x,temp_y) and arr[temp_x][temp_y] > curr and d[temp_x][temp_y] == 0:
            x = temp_x
            y = temp_y
            break

    # 업데이트 안되면 종료
    if curr == arr[x][y] :
        break
for a in answer:
    print(a, end=" ")