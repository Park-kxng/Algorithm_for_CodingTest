n = int(input())
arr = []
curr = [0,0]

dx, dy = [0,1,0,-1],[1,0,-1,0]
for i in range(n):
    arr.append(list(map(int,input().split())))

def in_range(x,y):
    if 0<= x <n and 0<= y < n:
        return True
    else:
        return False
answer = 0
for i in range(n):
    for j in range(n):
        count = 0
        curr = [j,i]

        x = curr[0]
        y = curr[1]

        for dx_, dy_ in zip(dx,dy):
            x_ = x + dx_
            y_ = y + dy_
            if in_range(x_,y_) and arr[x_][y_] == 1:
                count += 1
        if count >= 3 :
            answer += 1

print(answer)


