import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
lst = []
record = []

def gcd_lst(n1, n2):
    global record
    if n2 == 0:
        return n1
    else:
        r, q = n1%n2 , n1//n2
        record.append([r,q])
        return gcd_lst(n2, r)

def gcd (n1,n2):
    if n2 == 0:
        return n1
    else:
        
        return gcd(n2, n1 % n2)

if c % gcd(a,b) != 0: # x,y가 존재하지 않는 경우
    print(-1)
else: # x,y가 존재하는 경우
    temp = gcd_lst(a,b)

    # x와 y 구하기
    x_ = 1
    y_ = 0
    for i in range(len(record)-1,-1,-1):
        q = record[i][1]
        x = y_
        y = x_-y_* q

        x_ = x
        y_ = y
    k = c / temp 
    x = int(k*x)
    y = int(k*y)
    print(x,y)
