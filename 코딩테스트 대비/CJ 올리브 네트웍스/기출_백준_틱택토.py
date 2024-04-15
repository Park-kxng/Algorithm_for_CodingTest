import sys
sys.stdin = open("input.txt",'r')

a = []
answer = []

while True:
    temp = input()
    if len(temp) == 3:
        break
    a.append((temp))



# 꽉 찬 경우 > 갯수 확인
# 꽉 차지 않은 경우 > 갯수 확인과 빙고한 사람이 있는지 확인

def check_bingo(arr):
    temp = [arr[0:3],arr[3:6],arr[6:9]]
    check_lst = []
    arr_countX = arr.count('X')
    arr_count0 = arr.count('O')

    # 가로, 세로
    for i in range(0,3):
        check_lst.append(temp[i])
        check_lst.append([temp[0][i],temp[1][i],temp[2][i]])
    # 대각선
    check_lst.append([temp[0][0], temp[1][1], temp[2][2]])
    check_lst.append([temp[2][0], temp[1][1], temp[0][2]])

    return_value = False
    x_wins = o_wins = 0

    for check in check_lst:
        countX = check.count('X')
        count0 = check.count('O')

        if countX == 3:
            x_wins += 1

        if count0 == 3:
            o_wins += 1

    if x_wins>0 and o_wins>0 :
        return False
    if x_wins>0 :
        return arr_countX == arr_count0 + 1
    if o_wins>0 :
        return arr_countX == arr_count0

    if arr_countX + arr_count0 == 9 :
        return arr_countX == arr_count0 + 1

def check_answer(possible):
    if possible:
        return "valid"
    else:
        return "invalid"



for curr_time in a:

        answer.append(check_answer(check_bingo(curr_time)))

    # 게임 종료

for ans in answer:
    print(ans)

