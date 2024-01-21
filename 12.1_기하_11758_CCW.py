import sys
input = sys.stdin.readline
points = []
for i in range(3):
    x, y = map(int, input().split())
    points.append([x,y])

x1, y1  = points[0][0], points[0][1]
x2, y2  = points[1][0], points[1][1]
x3, y3  = points[2][0], points[2][1]

ccw = (x1*y2 +x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)
if ccw<0: #시계방향
    print(-1)
elif ccw == 0: # 일직선
    print(0)
elif ccw >0 : # 반시계방향
    print(1)

