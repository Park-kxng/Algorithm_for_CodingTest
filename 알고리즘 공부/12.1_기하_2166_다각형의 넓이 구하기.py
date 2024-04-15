import sys
input = sys.stdin.readline

n = int(input())
points = [[0,0] for _ in range(n)]
for i in range(n):
    points[i][0], points[i][1] = map(int, input().split())

points.append([points[0][0], points[0][1]])
ccw = 0

for i in range(n):
    ccw += (points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1])

answer = abs(ccw)/2
print(round(answer,2))
