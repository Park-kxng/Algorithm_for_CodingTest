# n = 3
# answer = []
# def print_answer():
#     for elem in answer:
#         print(elem, end = " ")
#     print()
#
# def choose(curr_num):
#     print("answer--------", answer)
#     if curr_num == n+1 :
#         print_answer()
#         return
#
#     answer.append(0)
#     choose(curr_num+1)
#     answer.pop()
#
#     answer.append(1)
#     choose(curr_num+1)
#     answer.pop()
#
#
#
# choose(1)

k, n = map(int, input().split())
answer = []
def print_answer():
    for str in answer :
        print( str , end = " ")
    print()

def choose (curr_num):
    if curr_num == n+1 :
        print_answer()
        return
    for i in range(1,k+1):
        answer.append(i)
        choose(curr_num+1)
        answer.pop()
    return

choose(1)























