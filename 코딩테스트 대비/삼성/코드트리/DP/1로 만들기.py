n = int(input())
# 최소인 경우를 만드는 것이 포인트임
d = [0] * 30001

for i in range(2,n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i],d[i//5]+1)


print(d[n])