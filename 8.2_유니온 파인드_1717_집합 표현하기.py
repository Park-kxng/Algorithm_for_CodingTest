import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
# m 입력으로 주어지는 연산의 갯수
# n : 집합의 개수 -> 초기는 n+1개 있음

# 0,a,b = 합집합 연산 진행
# 1 a b = 같은 집합 안에 있나요?

parent = [i for i in range(n+1)]
d = []
inp =[]
lead = 0
def find(a):
    global parent
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def match(a,b):
    global parent
    if find(a) == find(b):
        return('YES')
    else:
        return('NO')


def union(a,b):
    global parent
    if find(a) != find(b):
        parent[b] = a
        

for i in range(m):
    op, a, b = map (int, input().split())
    inp.append([op, a, b])

for i in range(m):
    op = inp[i][0]
    a = inp[i][1]
    b = inp[i][2]

    if op == 1:
        print(match(a,b))
    elif op == 0 :
        union(a,b)
