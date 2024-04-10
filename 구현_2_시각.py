n = int(input())

h = 0
m = 0
s = 0

answer = 0

# 3중 반복문을 통해 해결 가능함.
for h in range(0,n+1):
    for m in range(0,60):
        for s in range(0,60):
            n_ = str(n)
            if n_ in list(str(h)) or n_ in list(str(m)) or n_ in list(str(s)):
                print(h,m,s)
                answer += 1

print(answer)