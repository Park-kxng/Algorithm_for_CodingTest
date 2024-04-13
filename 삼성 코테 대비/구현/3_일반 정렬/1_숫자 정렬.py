n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)


for _ in range(0,2):
    for i in arr:
        print(i,end=" ")
    arr.sort(reverse = True)
    print()