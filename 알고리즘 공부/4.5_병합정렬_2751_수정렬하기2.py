import sys

# 값 입력받기
input = sys.stdin.readline
n = int(input())
a = [0] * int(n+1)
for i in range(1,n+1):
    a[i] = int(input())
tmp = [0] * int(n+1)

# 병합 정렬
def merge_sort(s, e):
    if e-s < 1: return
    m = int(s+(e-s)/2)

    merge_sort(s, m)
    merge_sort(m+1,e)

    for i in range(s,e+1):
        tmp[i] = a[i]
    
    k = s
    index1 = s
    index2 = m+1

    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp [index2]:
            a[k] = tmp [index2]
            k+= 1
            index2 += 1
        else:
            a[k] = tmp[index1]
            k+= 1
            index1 += 1
    while index1 <= m:
        a[k] = tmp[index1]
        k+= 1
        index1 += 1
    while index2 <= e:
        a[k] = tmp[index2]
        k+= 1
        index2+= 1

merge_sort(1,n)
# 출력 : 정렬한 결과를 한 줄에 하나씩 출력
for i in range(1,n+1):
   print(str(a[i]))
