from collections import deque

n,m,k = map(int, input().split())
arr = []
set_arr = []
attack_count = [[0] * m for _ in range(n)] # 시점 0에서 이미 공격한 경험이  있음
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

class index_for_attack:
    def __init__(self,index, attack_count, nm, n):
        self.index = index
        self.attack_count = attack_count
        self.nm = nm
        self.n = n

def make_set(arr):
    temp = []
    for i in range(n):
        for j in range(m):
            temp.append(arr[i][j])
    set_arr = set(temp)
    return set_arr
def find_index(arr, value):
    temp = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == value:
                temp.append([i,j])
    return temp
def find_dead(arr):
    temp = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] < 0:
                arr[i][j] = 0
    return temp
def find_attack_index (arr, set_arr, type, check = 0):
    attack = []
    sort_minus = 0 # 차순 설정
    min_v = min(set_arr)
    max_v = max(set_arr)

    if type == 0 : # 공격자 선정
        sort_minus = -1
        attacks = find_index(arr, min_v)
    elif type == 1 : # 공격받는 자 선정
        sort_minus = 1
        attacks = find_index(arr, max_v)
    #print("break2-", attacks)
    if len(attacks) == 1: # 가장 낮은 포탑이 1개인 경우
        attack = attacks[0]
    elif len(attacks) >= 2: # 가장 낮은 포탑이 2개 이상인 경우
        # 객체 정렬 - 가장 최근 혹은 오래된 /  행과 열의 합 / 열의 값
        temp = []
        for a in attacks:
            n_ = a[0]
            m_ = a[1]
            temp.append(index_for_attack(a,attack_count[n_][m_],n_+m_,n_ ))
        temp.sort(key=lambda x :(sort_minus * x.attack_count, sort_minus * x.nm, sort_minus * x.n))
        if type == 1 and temp[0].index == check:
            attack = temp[1].index
        else:
        #print("break3-",temp[0])
            attack = temp[0].index
    return attack
# 격자 안에 있는지 확인하는 함수
def in_range(x,y):
    if 0<= x < n and 0 <= y < m :
        return True
    else:
        return False
# 가장자리인지 파악 후, 반대편으로 나오도록 하는 함수
def not_in_range_index (index, standard):
    if index < 0:
        index = standard - 1
    elif index == standard:
        index = 0
    return index

# 레이저 공격을 위한 최단 경로 찾기
def BFS(arr,visited,start,end):
    q = deque([start])
    order = []
    while q:
        curr_v = q. popleft()
        #print("curr_v", curr_v)
        x,y = curr_v[0], curr_v[1]
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 우하좌상 순서대로 움직이기

        
        for dx, dy in zip(dxs, dys):
            x_, y_ = x + dx, y+ dy
            if in_range(x_,y_) and not visited[x_][y_] and arr[x_][y_] != 0 : # 방문한 적 없고, 무너진 포탑이 아닌 경우
                visited[x_][y_] = True
                order.append([x_,y_])

                if visited[end[0]][end[1]] == True:
                    return order
                q.append([x_,y_])
                break




    return []
def plus_attack(init, arr):
    for i in range(n):
        for j in range(m):
            if init[i][j]!= 0 and init[i][j] == arr[i][j]: # 변한 게 없는 경우
                arr[i][j] += 1
def check_stop(arr):
    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 :
                count += 1
    if n*m - count == 1:
        return True
    else:
        return False
for k_ in range(k):
    # 4번에서 비교를 위해 처음의 공격력 리스트 저장
    init_attack = [list(inner) for inner in arr]
    # 1. 공격자 선정 -----------------------
    set_arr = make_set(arr)
    set_arr.remove(0) # 무너진 포탑 제외
    #print("break 1- ",arr,set_arr)
    attack = find_attack_index(arr,set_arr,0)
    # 공격자의 공격력 증가
    x ,y = attack[0], attack[1]
    arr[x][y] += (n+m)
    attack_count[x][y] = k+1 # 지금 턴을 업데이트 함. (최근 공격 여부 업데이트)
    attack_value = arr[x][y]
    #print("attack_value", attack_value)
    #print("attack", attack)

    # 2. 공격자의 공격 -----------------------
    # 공격받는 자 선정
    attacked = find_attack_index(arr,set_arr,1)
    #print("attacked",attacked, arr[attacked[0]][attacked[1]])

    # 공격 실시
    visited = [[False]* m for _ in range(n)]
    orders = BFS(arr,visited,attack,attacked)
    #print("orders",orders)
    if len(orders) != 0: # 최단 거리가 있는 경우
        # 1) 레이저 공격
        #print("레이저 공격 실시!!")

        for order in orders:
            order_x, order_y = order[0], order[1]
            if order == attacked :
                arr[order_x][order_y] -= attack_value
            else:
                arr[order_x][order_y] -= (attack_value//2)


    else:
        #print("포탄 공격 실시!!")
        #print("arr", arr)
        # 2) 포탄 공격
        order_x, order_y = attacked[0], attacked[1]
        arr[order_x][order_y] -= attack_value
        # 주위의 8개의 방향에 있는 포탑도 피해를 입음
        attack_value = attack_value // 2 # 피해량 절반으로 줄음
        #print("attack_value 체인지 --> ",attack_value)
        # 8가지 방향 설정
        dxs ,dys = [1,-1,0,0,1,-1,1,-1],[0,0,1,-1,1,-1,-1,1]
        for dx, dy in zip(dxs, dys):
            x_ = not_in_range_index(order_x  + dx, n)
            y_ = not_in_range_index(order_y  + dy, m)
            #print(x_,y_)
            arr[x_][y_] -= attack_value

        #print("arr",arr)

    # 3. 포탑 부서짐 -----------------------
    find_dead(arr)
    #print("arr",arr)


    # 4. 무관한 포탑은 공격력 1을 얻는다
    plus_attack(init_attack, arr)
    #print(init_attack, arr)
    # 부서지지 않은 포탑이 1개인 경우 중지
    if check_stop(arr):
        break


# 공격이 다 끝난 후, 가장 강한 포탑의 공격력을 출력함
set_arr = make_set(arr)
best = find_attack_index(arr,set_arr,1)
print(arr[best[0]][best[1]])