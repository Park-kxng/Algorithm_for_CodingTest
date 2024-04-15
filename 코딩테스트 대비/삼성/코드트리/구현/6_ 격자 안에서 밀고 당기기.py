n,t = map(int,input().split())
arr = []
for i in range(2):
    temp = list(map(int, input().split()))
    if i == 1 :
        new = []
        for i in range(n-1,-1,-1):
            new.append(temp[i])
        temp = new
    arr.append(temp)

print(arr)
for t_ in range(t):
    temp1 = arr[0][n-1]
    for i in range(n-1,0,-1):
        arr[0][i] = arr[0][i-1]

    temp2 = arr[1][0]
    for i in range(0,n-1):
        arr[1][i] = arr[1][i+1]


    arr[0][0] = temp2
    arr[1][n-1] = temp1

new = []
for i in range(n-1,-1,-1):
    new.append(arr[1][i])
arr[1] = new

for a in arr :
    for i in range(n):
        print(a[i], end=" ")

    print()








