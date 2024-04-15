import sys
from collections import deque

input = sys.stdin.readline

# 1) 입력
n, m = map(int, input().split())
students = [[] for _ in range(n)]
d = [0 for _ in range(n)]  # 진입 차수 리스트
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    students[a-1].append(b)
    d[b-1] += 1

# 2) 위상 정렬로 학생 줄 세우기
for i in range(1, n+1):
    if d[i-1] == 0:
        q.append(i)

result = []

while q:
    cur_student = q.popleft()
    result.append(cur_student)

    for next_student in students[cur_student-1]:
        d[next_student-1] -= 1
        if d[next_student-1] == 0:
            q.append(next_student)

# 3) 출력: 학생들 줄 선 순서대로 출력하기
print(" ".join(map(str, result)))
