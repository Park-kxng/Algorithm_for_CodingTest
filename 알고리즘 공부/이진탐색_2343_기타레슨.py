import sys

input = sys.stdin.readline
N = int(input())
k = int(input())
start = 1
end = k
ans = 0
while start <= end:
  middle = int((start+end)/2)
  sum = 0
  for i in range(1,N+1):
    sum += min(int(middle/i),N)
  
  if sum < k :
    start = middle + 1
  elif sum >= k:
    ans = middle
    end = middle -1


print(start)