# 순열
nums = [1,2,3]
visited = [False] * len(nums)
new_arr = ""
# 순열
def permutations (nums, new_arr,n):

    if len(new_arr) == n:
        print(new_arr)
        return

    for i in range(0, len(nums)):
        if not visited[i]:
            visited[i] = True
            permutations(nums, new_arr + str(nums[i]), n)
            visited[i] = False
# 중복 순열
def generate_permutations(nums, new_arr, n):
    if len(new_arr) == n:
        print(new_arr)
        return

    for i in range(0,len(nums)):
        generate_permutations(nums, new_arr + str(nums[i]), n)
# 조합
def combinations(nums, new_arr, n, cnt):
    if len(new_arr) == n:
        print(new_arr)
        return

    for i in range(cnt,len(nums)):
        combinations(nums,new_arr + str(nums[i]), n, i + 1)
# 중복 조합
def combinations(nums, new_arr, n, cnt):
    if len(new_arr) == n:
        print(new_arr)
        return

    for i in range(cnt,len(nums)):
        combinations(nums,new_arr + str(nums[i]), n, i)
