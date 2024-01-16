import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# DFS 탐색
def DFS(num):
    visited[num] = True
    for i in tree[num]:
        if not visited[i]:
            answer [i] = num
            DFS(i)
DFS(1)

for i in range(2,n+1):
    print(answer[i])