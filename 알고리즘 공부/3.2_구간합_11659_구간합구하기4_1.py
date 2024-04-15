import sys

# n,m 입력받기
N, M = map(int, input().split())
# 리스트 입력받기
List = list(map(int, input().split()))
prefix = [0] * N
prefix[0] = List[0] # 첫번째 값을 넣어줌
for i in range(1, N): # 두번째 값부터 누적합을 저장
    prefix[i] = prefix[i-1] + List[i]

queries = []
for i in range(M):
    # n,m 입력받기
    n, m = map(int, input().split())
    queries.append((n, m))

for query in queries:
    N, M = query
    if N == 1:
        sys.stdout.write(str(prefix[M-1]) + "\n")
    else:
        sys.stdout.write(str(prefix[M-1] - prefix[N-2]) + "\n")

