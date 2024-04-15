import sys

print = sys.stdout.write
a = list(input())  # 개행 문자를 제거하고 각 문자를 정수로 변환하여 리스트에 저장


# 내림차순으로 정렬하기
for j in range(len(a)):
    maxIndex = i
    for i in range(j+1,len(a)):
        if a[maxIndex] < a[i]: # 최댓값을 찾습니다.
            maxIndex = i
    #최댓값을 가장 앞으로 옮깁니다.
    
    if a[j] < a[maxIndex]:
        temp = a[j]
        a[j] = a[maxIndex]
        a[maxIndex] = temp


for i in range(len(a)):
    print(str(a[i]))

     
    

