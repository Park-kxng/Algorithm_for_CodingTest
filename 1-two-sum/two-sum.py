class Solution(object):
    def twoSum(self, nums, target):
        answer = []
        # 1차원 리스트이므로 N 복잡도로 구성함.
        for i in nums:
            # i 일때 다른 요소들 중 타겟을 만족시킬 수 있는 항목이 있는지 확인
            find = target - i
            # 지금 있는 요소를 뺀 리스트를 생성
            list_temp = nums[:]
            list_temp[list_temp.index(i)] = ""
            
            # 만족하는 항목이 있는 경우
            if find in list_temp:
                answer.append(nums.index(i))
                answer.append(list_temp.index(find))
                break
            # 없는 경우
            else : 
                continue


        return answer
        