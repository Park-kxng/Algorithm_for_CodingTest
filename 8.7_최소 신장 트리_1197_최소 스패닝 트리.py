import sys
from collections import deque
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edge = []
for i in range(e):
    a,b,c = map(int, input().split())
    edge.append([a,b,c]) 

edge.sort(key=lambda x: x[2]) # c를 기준으로 오름차순으로 정렬하기

def find(a):
    global parent
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    global parent
    parent[b] = find(a)


edge_num = 0
answer =[]
for i in range(len(edge)):
    start = edge[i][0]
    end = edge[i][1]
    value = edge[i][2]
    find_start =find(start)
    find_end = find(end)

    if len(answer)-1 == v-1:
        break
    if find(start) != find(end):
        union(start,end)
        answer.append(value)

sum = 0
for i in answer:
    sum += i

print(sum)