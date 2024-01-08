def find_next_greater_elements(nums):
    stack = []
    result = [-1] * len(nums)  # 결과를 저장할 리스트, 기본값은 -1로 초기화

    for i in range(len(nums)):
        # 스택이 비어있지 않고 현재 원소가 스택의 가장 위 원소보다 큰 경우
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()  # 스택의 가장 위 원소의 인덱스
            result[idx] = nums[i]  # 현재 원소가 해당 인덱스의 오큰수가 됨

        stack.append(i)  # 현재 원소의 인덱스를 스택에 추가

    return result

# 입력 받기
N = int(input())
A = list(map(int, input().split()))

# 오큰수 찾기
NGE_result = find_next_greater_elements(A)

# 결과 출력
for result in NGE_result:
    print(result, end=" ")