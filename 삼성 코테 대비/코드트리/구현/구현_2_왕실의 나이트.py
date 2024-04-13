# 체스판 8*8
# 나이트는 L자 형태로만 이동 가능
# 1) 수평 2칸 수직 1칸
# 2) 수직 2칸 수평 1칸

# 행(수직) - 1~8, 열(수평) - a~h

start = input()
row,start_col = start[0], start[1]
move_row =[ [0,-1],[0,1]]
move_col =[ [-1,0],[1,0]]

row_int = ['a','b','c','d','e','f','g','h']
for i in row_int :
    if row == i:
       start_row = row_int.index(row)+1
row_time = 0
col_time = 0
answer = 0
for i in range(1,3):
    row_time = i
    if row_time == 1 :
        col_time = 2
    else:
        col_time = 1

    now_row = 0
    now_col = 0
    for r in move_row:
        for c in move_col:

            now_row = start_row + row_time * r[0] + col_time * c[0]
            now_col = int(start_col) + row_time * r[1] + col_time * c[1]
            
            if 1<= now_row <= 8 and 1<=  now_col <= 8:
                answer += 1
print(answer)