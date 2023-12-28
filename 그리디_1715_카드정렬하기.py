import sys
from queue import PriorityQueue

N = int(input())
pq = PriorityQueue()

for i in range(N):
    card = int(input())
    pq.put(card)

data1 = 0
data2 = 0
sum = 0

while pq.qsize() > 1:
  data1 = pq.get()
  data2 = pq.get()
  temp = data1 + data2
  sum += temp
  pq.put(temp)

print(sum)