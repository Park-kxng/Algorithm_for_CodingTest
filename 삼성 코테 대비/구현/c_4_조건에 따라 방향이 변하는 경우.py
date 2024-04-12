# 입력 받기
n, t = input().split(' ')
r,c,d = input().split(' ')

n = int(n)
t = int(t)
r = int(r)
c = int(c)
curr = [r-1,c-1]
direction = {'U':3,'D':1,'R':0,'L':2}
direction_change = {3:1,1:3,0:2,2:0}

curr_d = direction[d]
dx, dy = [0,1,0,-1],[1,0,-1,0] # +1 시계방향

def in_range(x,y):
    if 0<= x < n and 0 <= y < n :
        return True
    else:
        return False


for i in range(int(t)):

    x = curr[0]
    y = curr[1]

    x_ = x + dx[curr_d]
    y_ = y + dy[curr_d]

    if in_range(x_,y_):
        curr = [x_, y_]
    else:
        curr_d = direction_change[curr_d]

print(curr[0]+1, curr[1]+1)

