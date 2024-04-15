m1,m2 = input().split()
arr = [m1,m2]
cur = [0,0]
dx ,dy = [0,1,0,-1],[1,0,-1,0]
curr_d = 0

for m in arr :
    x = cur[0]
    y = cur[1]

    if m == 'L':
        curr_d = (curr_d - 1 + 4) % 4
    elif m == 'R':
        curr_d = (curr_d + 1) % 4
    elif m == 'F':
        x = x + dx[curr_d]
        y = y + dy[curr_d]

        cur = [x,y]

print(cur[0], cur[1])