# 정수 N을 입력받아 1부터 N까지의 숫자 중에서
# 합이 10이 되는 조합을 리스트로 반환하는 solution 함수를 작성하세요.

def solution(num):

    answer = []

    def backtrack(sum, selected_nums, start):
        if sum == 10 :
            answer.append(selected_nums)
            return
        for i in range(start,num+1):
            if sum + i <= 10:
                backtrack(sum+i, selected_nums+[i], i+1)
    backtrack(0,[],1)
    return answer
answer = solution(5)
print(answer)