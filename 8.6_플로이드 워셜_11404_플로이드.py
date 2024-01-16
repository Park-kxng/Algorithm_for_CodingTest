import sys
input = sys.stdin.readline

n = int(input()) #도시의 개수
m = int(input()) # 버스의 개수
bus = [[sys.maxsize for _ in range(n+1)]for _ in range(n+1)]
# 리스트 선언하고 초기화하기
for i in range(n+1):
    bus[i][i] = 0
  
# 버스 정보 입력받기
for i in range(m):
    a,b,c = map(int, input().split())
    if bus[a][b] > c : 
        bus[a][b] = c # 최솟값으로 업로드 (노선이 중복되서 나오는 경우)

# 점화식으로 리스트 업데이트하기
for city in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            bus[s][e] = min(bus[s][e], bus[s][city] + bus[city][e])

for i in range(1,n+1):
    for j in range(1,n+1):
        if bus[i][j] == sys.maxsize:
            print(0,end =' ')
        else:
            print(bus[i][j],end =' ')
    print()