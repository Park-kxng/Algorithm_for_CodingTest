n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


def bomb(arr, s, e):
    init_arr = arr.copy()

    # 폭탄 터짐
    for i in range(s-1,e):
        arr[i] = 0


    new = []
    for a in arr:
        if a != 0 :
            new.append(a)


    return new


for _ in range(2):
    s,e = map(int, input().split())
    arr = bomb(arr,s,e)

print(len(arr))
for a in arr:
    print(a)