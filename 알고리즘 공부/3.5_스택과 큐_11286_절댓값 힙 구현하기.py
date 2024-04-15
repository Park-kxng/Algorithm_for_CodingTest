import sys
from queue import PriorityQueue

print = sys.stdout.write
input = sys.stdin.readline

pq = PriorityQueue()
n = int(input())

for i in range(n):
    input_item = int(input())

    if input_item == 0:
        if pq.empty():
            print('0\n')
        else:
            _, val = pq.get()
            print(str(val) + '\n')
    else:
        pq.put((abs(input_item), input_item))
