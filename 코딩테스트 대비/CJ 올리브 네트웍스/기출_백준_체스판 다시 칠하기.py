import sys
sys.stdin = open("input.txt",'r')

n,m = map(int, input().split())
chess_dic = {'W' : 1, 'B': 0}
change = {1:0,0:1}
chess = [ list(input()) for i in range(n)]

# 백 : 1 , 검 : 0 으로 전처리
for i in range(n):
    for j in range(m):
        chess[i][j] = chess_dic[chess[i][j]]

def in_range(i,j):
    return 0 <= i < n and 0 <= j < m
def check_smaller(num1, num2):
    return num1 if num1 <= num2 else num2

def check_rewrite (i,j):
    start_x , start_y = i, j

    b = chess[i][j] # 0,0 위치에 있는 색상
    w = change[b] # b의 반대색상

    answer , answer2 = 0, 0
    #print(i,j,"--",i+7,j+7, ":",end = '')

    for i in range(8):
        for j in range(8):
            x = start_x + i
            y = start_y + j
            # print(i,j,chess[x][y])
            if i % 2 == 0:
                if j % 2 == 0:
                    if chess[x][y] != b:
                        # print("log1",x,y)
                        answer += 1
                else:
                    if chess[x][y] != w:
                        # print("log2",x,y)
                        answer += 1
            else:
                if j % 2 == 0:
                    if chess[x][y] != w:
                        # print("log3",x,y)
                        answer += 1
                else:
                    if chess[x][y] != b:
                        # print("log4",x,y)
                        answer += 1
    for i in range(8):
        for j in range(8):
            x = start_x + i
            y = start_y + j
            if i % 2 == 0:
                if j % 2 == 0:
                    if chess[x][y] != w:
                        answer2 += 1
                else:
                    if chess[x][y] != b:
                        answer2 += 1
            else:
                if j % 2 == 0:
                    if chess[x][y] != b:
                        answer2 += 1
                else:
                    if chess[x][y] != w:
                        answer2 += 1


    return check_smaller(answer,answer2)



    # 검정색으로 시작하는 경우

answer = -1
for i in range(n):
    for j in range(m):
        if not in_range(i+7, j+7):
            continue
        # 다시 칠해야 하는 정사각형의 갯수
        if answer == -1:
            answer = check_rewrite(i,j)
            continue
        temp = check_rewrite(i,j)
        answer = check_smaller(answer, temp)


print(answer)