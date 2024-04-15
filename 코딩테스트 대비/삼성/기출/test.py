
# 직사각형 회전

def rotated_90(a):
    m = len(a)
    n = len(a[0])

    result = [[0]*m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            result[j][m-i-1] = a[i][j]

def rotated_180(a):
    m = len(a)
    n = len(a[0])

    result = [[0]*m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            result[n-i-1][m-j-1] = a[i][j]

def rotated_270(a):
    m= len(a)
    n  = len(a[0])

    result = [[0]*m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[m-j-1][i] = a[i][j]

# 순열 및 조합
arr = [1,2,3,4]
visited = [0] * len(arr)
# 순열
def permutations(n, new_arr):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, new_arr + arr[i])
            visited[i] = 0

# 중복 순열
def product(n, new_arr):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        product(n, new_arr + arr[i])

# 조합
def combinations(n, new_arr, cnt):
    global arr

    if len(new_arr) == n :
        print(new_arr)
        return
    for i in range(cnt,len(arr)):
        combinations(n,new_arr + arr[i], i+1)
# 중복 조합
def combinations_with_replacemane(n, new_arr, cnt):
    global arr

    if len(arr) == n :
        print(new_arr)
        return
    for i in range(cnt, len(arr)):
        combinations_with_replacemane(n, new_arr + arr[i], i)