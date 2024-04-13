n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
def in_range(x,y):
    if 0<= x < n and 0<= y < n:
        return True
    else :
        return False
sum = 0
for i in range(n):
    for j in range(n):

        if in_range(i+2, j+2):
            temp = 0
            for i_ in range(i,i+3):
                for j_ in range(j,j+3):
                    temp += arr[i_][j_]

            if temp > sum :
                sum = temp
print(sum)