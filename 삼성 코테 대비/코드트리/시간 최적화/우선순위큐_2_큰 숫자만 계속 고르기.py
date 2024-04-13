import heapq
n,m = map(int, input().split())
arr = list(map(int, input().split()))

q = []
for s in arr :
    heapq.heappush(q,-s)



for _ in range(m):
    max_val = - heapq.heappop(q)
    heapq.heappush(q,-(max_val-1))

    
print(-q[0])