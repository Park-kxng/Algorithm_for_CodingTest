# N * N 정사각형 , 가장 왼쪽 위는 (1,1)
# L, R, U, D
# 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.
n = int(input())
plan = input().split()
x ,y = 1,1 # 초기화
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for p in plan:
    for i in range(len(move_types)):
        if p == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n :
        continue # 공간을 벗어나는 경우는 무시한다.
    x, y  = nx , ny
print(x,y)