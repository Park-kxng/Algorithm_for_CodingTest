import sys

# 1) 변수 초기화 및 N,M을 입력받습니다.
input = sys.stdin.readline
N, M = map(int, input().split())
A = [[0]*(N+1)]
D = [[0]*(N+1) for _ in range(N+1)]
answer = 0

# 2) 표에 채울 수를 N번 동안 입력받습니다.
for i in range(N):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

    
# 3) 2번 단계에서 입력받은 수를 기반으로 누적합 리스트를 완성한다

for i in range(1 ,N+1):
    for j in range(1,N+1):
       D[i][j] = A[i][j]+ D[i-1][j] + D[i][j-1] - D[i-1][j-1]

# 4) 누적합 리스트를 이용해 x1,y1에서 x2,y2까지의 수의 합을 구합니다
answer_list = []
for i in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    answer = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    answer_list.append(answer)

for answer in answer_list:
    print(answer)