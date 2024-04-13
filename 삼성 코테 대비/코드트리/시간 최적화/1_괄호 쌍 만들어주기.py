arr = list(input())

set1 = [0] * len(arr)

count = 0
for i in range(len(arr)-1):
    if arr[i] == '(' and arr[i+1] == '(':
        set1[i+1] = 1
sum = 0
set1_cnt = 0
for i in range(len(arr)-1):
    if set1[i] == 1:
        set1_cnt += 1
    if arr[i] == ')' and arr[i + 1] == ')':
        sum += set1_cnt

print(sum)
