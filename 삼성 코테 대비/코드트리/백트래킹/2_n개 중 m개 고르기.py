n, m = map(int, input().split())
answer = []
def print_answer():
    for ans in answer:
        print(ans, end= " ")
    print()

def choose(curr_num, count):
    if count == m:
        print_answer()
        return

    for i in range(curr_num + 1,n+1):
        answer.append(i)
        choose(i+1, count +1)
        answer.pop()


for i in range(1,n+1):
    answer.append(i)
    choose(i,1)
    answer.pop()