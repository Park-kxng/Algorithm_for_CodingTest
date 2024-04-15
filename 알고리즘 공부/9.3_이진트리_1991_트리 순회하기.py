import sys

input = sys.stdin.readline
# 입력
n = int(input())
tree = {}

for i in range(n):
    root,left,right = map(str, input().split()) #현재 노드, 왼쪽 노드, 오른쪽 노드
    tree[root] = [left, right]

def preOrder(now):
    if now == '.':
        return
    print(now,end='')
    print(tree[now][0]) # 왼쪽 탐색
    print(tree[now][1]) # 오른쪽 탐색

def inOrder(now):
    if now == '.':
        return
    print(tree[now][0]) # 왼쪽 탐색
    print(now,end='')
    print(tree[now][1]) # 오른쪽 탐색


def postOrder(now):
    if now == '.':
        return
    
    print(tree[now][0]) # 왼쪽 탐색
    print(tree[now][1]) # 오른쪽 탐색
    print(now,end='')   


# 공백없이 출력
# 전위순회
preOrder('A')
print()
# 중위순회
inOrder('A')
print()
# 후위순위
postOrder('A')
    

