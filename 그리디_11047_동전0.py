import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
answer = 0
for i in range(N):
  temp_coin = int(input())
  coin.append(temp_coin)


coin.sort(reverse = True)

for i in coin:
  if K > i :
    
    num =  K // i
    answer += num
    K -= num * i

print(answer)