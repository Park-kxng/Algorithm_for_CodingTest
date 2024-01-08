import sys
input = sys.stdin.readline
N = int(input())
A = []
# 입력받은 수열
for i in range(N):
    item = int(input())
    A.append(item)
# 스택에 push 하는 순서는 반드시 오름차순을 지키도록 해야 함
# 스택 연산 수행 방법
stack = []
# 처음 시작
for i in range(A[0]):
    stack.append(i+1)

#print(stack)    
last_num = 0
answer = []
right = 1
for i in range(len(A)): # 두번째 부터

    while last_num < A[i]:
        last_num += 1
        stack.append(last_num)
        answer.append('+')
    
    if stack[-1] == A[i]:
        last_num = stack.pop()
        answer.append('-')
    else:
        answer = ['NO']
        break



if answer == 0:
    print('NO')
else:
    for ans in answer:
        print(ans)
