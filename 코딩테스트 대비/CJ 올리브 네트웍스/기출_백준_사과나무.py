import sys
sys.stdin = open("input.txt",'r')

# 입력 받기
n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)] # 사과를 통해 얻은 이익, 노동비 = 총이익 정리

# 1 <= K <= n : 농부 형곤이가 가져갈 수 있는 정사각형의 모양
answer = 0
# DP - 총이익의 합을 메모제이션하기
# -> 완전 탐색, 모든 경우의 수를 다 확인해야 함. 겹치는 연산이 많음

# 메모제이션 실시
sum = [[0] *n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j == 0 :
            sum[i][j] = apple[i][j]
        elif j == 0:
            sum [i][0] = sum [i-1][0] + apple[i][j]
        elif i == 0:
            sum [0][j] = sum [0][j-1] + apple[i][j]
        else:
            sum[i][j] = apple[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]


def check_bigger(n1, n2):
    if n1 >= n2 :
        return n1
    if n2 > n1 :
        return n2
def in_range(i,j):
    return 0 <= i < n and 0<= j < n

answer = sum[0][0]

for k in range(1,n):
    for i in range(n):
        for j in range(n):
            if i < k-1 or j < k-1:
                continue
            if k == 1:
                temp = apple[i][j]
            else:
                temp = sum[i][j]

                check1 = in_range(i-k,j)
                check2 = in_range(i,j-k)

                if check1:
                    temp -= sum[i - k][j]

                if check2:
                    temp -= sum[i][j - k]

                if check1 and check2:
                    temp  += sum[i - k][j - k]
            #print(temp)
            answer = check_bigger(answer, temp)

# 최대 총익을 안겨주자
print(answer)
