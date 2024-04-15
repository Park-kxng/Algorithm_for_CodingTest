import sys
input = sys.stdin.readline

def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)

t = int(input())
lst = []
for i in range(t):
    a, b = map(int, input().split())
    lst.append([a,b])
   
for i in range(t):
    a,b = lst[i][0], lst[i][1]
     # Calculate GCD
    temp2 = gcd(b, a)

    # Calculate LCM
    temp = a * b // temp2
    
    print(temp)