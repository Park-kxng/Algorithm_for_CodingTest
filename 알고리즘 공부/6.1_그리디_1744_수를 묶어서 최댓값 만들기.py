from queue import PriorityQueue
n = int(input())
pq_plus = PriorityQueue()
pq_minus = PriorityQueue()
one = 0
zero = 0
sum = 0

for i in range(n):
    data = int(input())
    if data > 0:
        if data == 1:
            one += 1
        else :
            pq_plus.put(data*-1)
    elif data == 0:
        zero += 1
    elif data < 0 :
        pq_minus.put(data)



while pq_plus.qsize() >1:
    first =  pq_plus.get() * -1
    second =  pq_plus.get() * -1
    sum += first * second

if pq_plus.qsize()>0 :
    sum += pq_plus.get() * -1

while pq_minus.qsize() >1:
    first =  pq_minus.get() * -1
    second = pq_minus.get() * -1
    sum +=  first() * second

if pq_minus.qsize() > 0 :
    if zero != 1 :
        sum += pq_minus.get()
sum += one

print(sum)