import sys

input = sys.stdin.readline
n,m = map(int, input().split())
textList = set([input().rstrip() for _ in range(n)])
count = 0

for i in range(m): # 검사해야 하는 문자열들
    subText = input().rstrip()
    if subText in textList:
        count += 1

print(count)