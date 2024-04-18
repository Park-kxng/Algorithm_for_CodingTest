import sys

sys.stdin = open("input.txt",'r')

n, m, k = map(int, input().split())
winds = [ list(map(int, input().split())) for _ in range(n)]
curr = [ [0] * m for _ in range(n)]

# 0 : 빈칸, 1: 오른쪽, 2:왼쪽 , 3:위, 4: 아래, 5: 온도 조사
# 조사해야 하는 칸의 인덱스 저장
check = []
hitter = []
for i in range(n):
    for  j in range(m):
        if winds[i][j] == 0:
            continue

        if winds[i][j] == 5:
            check.append([i,j])
        else:
            hitter.append([i,j,(winds[i][j]+3)%4])





w = int(input())
wall = [list(map(int, input().split())) for _ in range(w)]




dxs, dys = [0,0,-1,1],[1,-1,0,0] # 오, 왼, 위, 아

chocolate = 0 # 구사과가 먹는 초콜릿
def update(x, y, value ,curr,d):
    if 0 <= x < n and 0 <= y < m :
        curr[x][y] = value

    # for c in curr : print(c)
    # print()



def wind_come(curr, hit):

    # t가 0인 경우 (x, y)와 (x-1, y) 사이에 벽이 있는 것이고,
    # t가 1인 경우에는 (x, y)와 (x, y+1) 사이에 벽이 있는 것

    start_x, start_y, d = hit[0], hit[1], hit[2]
    print("현재 --> ",start_x,start_y, d )
    # 히터에서 바람이 나옴 (x,y,방향)
    for i in range(5,-1,-1):

        x = start_x + dxs[d]
        y = start_y + dys[d]

        update(x, y, i, curr)

        for j in range(1,i):
            if d == 0 or d == 1:
                update(x +  j, y + dxs[d] * j, i-j, curr,d)
                update(x - j, y + dxs[d] * j, i-j, curr,d)

            if d == 2 or d == 3:
                update(x + dxs[d] * j, y + j, i-j, curr,d)
                update(x + dxs[d] * j, y - j, i-j, curr,d)


    for c in curr : print(c)

    return curr
def check_tempature(check, k):
    for c in check:
        x , y = c[0], c[1]
        if curr[x][y] < k :
            return False
    return True

# while True:
# 1. 집에 있는 온풍기에서 바람이 1번 나옴
print(wall)
for hit in hitter:
    wind_come(curr, hit)
# 2. 온도가 조절됨

# 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소

# 4. 초콜릿을 하나 먹음
chocolate += 1

# 5. 조사하는 모든 칸의 온도가 k 이상인지 검사. -> k이상 이면 중단 / 아니면 다시 1번으로 돌아감
if check_tempature(check,k):
    print("stop")
    # break

print(chocolate)