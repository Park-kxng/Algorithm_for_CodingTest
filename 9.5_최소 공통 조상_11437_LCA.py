import sys
from collections import deque
# 1) 입력 : 트리상에서 연결된 두 노드 주어짐
input = sys.stdin.readline()
print = sys.stdout.write()
n = int(input())
tree = [ [] for i in range(n+1)] # 인덱스 0번은 사용하지 않음
visited = [ False for i in range(n+1)]
depth = [0] * (n+1)
parent = [0] * (n+1)


for i in range(n-1):
    a,b = map(int, input().split())
    # 인접리스트로 구현하기 - 트리양방향 그래프로 간주함
    tree[a].append(b)
    tree[b].append(a)

# 2) 탐색 알고리즘으로 노드의 깊이 구하기
def DFS(num):
    q = deque()
    q.append(num)
    visited[num] = True
    level  =1
    now_size = 1
    count = 0
    while q:
        now_node = q.popleft()
        for next in tree[now_node]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                parent[next] = now_node
                depth[next] = level
        count += 1
        if count == now_size:
            count = 0
            now_size = len(q)
            level+= 1        
DFS(1)

def matchParent(a,b):
    if depth[a] < depth [b]:
        temp = a
        a = b
        b = temp
    
    while depth[a] != depth[b]:
        a = parent[a]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a
 
    
#  4) 두 노의 가장 가까운 공통 조상 출력하기
m = int(input())
for i in range(m):
    a,b = map(int, input().split())
    print(str(matchParent(a,b)))
    print('\n')