n,m = map(int,input().split())
a,b,direction =  map(int,input().split())
move_type = [[-1,0],[0,1],[1,0],[0,-1]]
def check_move(num):
    if num == 0 :
        return 3
    else:
        num = num - 1
        print(num)
        return num

# 0 북 ↑ , 1 동 → , 2 남 ↓, 3 서 ←
d = [[0] * m for _ in range(n)]
d[a][b] = 1 # 처음 간 위치 초기화


# 게임 맵 저장
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
# 게임 종료하게 하는 요소 초기화
allVisited = False
allSea = False
num = 0
done = True

while done:
    num += 1

    # 움직임 업데이트 (반시계 방향으로 90도 이동)
    curr_d = direction-1
    if curr_d == -1 :
        curr_d = 3
    dx = move_type[curr_d][0]
    dy = move_type[curr_d][1]
    # 게임 종료 여부 확인 (4면이 가봤거나 바다로 되어 있는 경우)
    case_1 = arr[a-1][b] == 1 or d[a-1][b] == 1
    case_2 = arr[a+1][b] == 1 or d[a+1][b] == 1
    case_3 = arr[a][b+1] == 1 or d[a][b+1] == 1
    case_4 = arr[a][b-1] == 1 or d[a][b-1] == 1


    if case_1 and case_2 and case_3 and case_4 :
        if curr_d%2 == 0: # 짝수 - 북,남, 0
            if dx == 1:
                dx = -1
            else :
                dx = 1

        else: # 홀수 - 동,서 1
            if dy == 1:
                dy = -1
            else:
                dy = 1
        if arr[a+dx][b+dy] == 1:
            done = False
        else :
            # 위치 업데이트
            a = a+dx
            b = b+dy
    else:
        # 육지이고, 가본 적 없는 경우
        if arr[a + dx][b + dy] == 0 and d[a+dx][b+dy] == 0:
            # 위치 업데이트
            a = a+dx
            b = b+dy
            # 방문 여부 업데이트
            d[a][b] = 1
        direction = curr_d



    
    
    

# 방문한 칸의 수 세기
answer = 0
for i in range(n):
    for j in range(m):
        if d[i][j] == 1:
            answer += 1


print(answer)

from collections import  deque
q = deque()
