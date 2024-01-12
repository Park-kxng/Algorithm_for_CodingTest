import sys
input = sys.stdin.readline

def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)


a,b = map(int, input().split())
lst =[a,b]
lst.sort()
repeat = int(gcd(lst[0],lst[1]))
print('1'*repeat)
