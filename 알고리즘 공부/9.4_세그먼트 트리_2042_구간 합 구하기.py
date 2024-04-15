import sys

input = sys.stdin.readline

# 세그먼트 트리 - 업데이트하고 구간합 구하기

n, m, sum = map(int,input().split()) # 수의 갯수, 수의 변경, 구간합을 구하는 횟수
change = []
for i in range(1,63):
    if 2**i>= n:
        k = i
        break
num = [0 for i in range(2**(k+1))]  

for i in range(2**k,2**k+n): # 주어진 수
    temp = int(input())
    num[i] = temp

for i in range(m+sum): # 수의 변경
    a,b,c = map(int, input().split())
    change.append([a,b,c])


# 구간합 구하기
for i in range(2**k-1,0,-1):
    num[i] = num[2*i] + num[2*i +1]
def changeBC(b,c):
    b_index = b + 2**k -1
    num[b_index] = c # 변경

    # 다른 데이터 업데이트 (구간합)
    # 오른쪽 왼쪽인지 확인
    hello = 1
    while hello == 1:
        temp = int(b_index%2)
        if temp == 1: # 오른쪽 노드
            parent_index = int((b_index-1)/2)
            num[parent_index] = num[b_index-1] + num[b_index]
        if temp == 0: # 왼쪽 노드
            parent_index = int(b_index/2)
            num[parent_index] = num[b_index] + num[b_index+1]

        b_index = parent_index
        if b_index == 1:
            hello = 0

def printSum(b,c):
    sum = 0
    start = b + 2**k -1
    end = c + 2**k -1
    while end >= start:
        if int(start%2) == 1: # 선택한다
            sum += num[start]

        if int(end %2) == 0: # 선택한다
            sum += num[end]
        
        start = int((start +1)/2)
        end = int((end-1)/2)

    print(sum)

for i in range(m+sum): # 수의 변경
    op = change[i][0]
    b = change[i][1]
    c = change[i][2]

    if op == 1:
        # b->c 로 바꾸기
        changeBC(b,c)
    elif op == 2:
        # 인덱스 b부터 c까지 합 출력하기
        printSum(b,c)
    
