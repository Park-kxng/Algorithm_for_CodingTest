
stack = []
mapping = {"}":"{","]":"[",")":"("}

c = "(){}[}"

def my_sol (c):
    for char in c:
        if char in mapping.keys(): # 닫힌 경우
            if stack == []:
                top_element = "#"
            else:
                top_element = stack.pop()
            if mapping[char] != top_element:
                return False



        else:
            stack.append(char)
    return True
print(my_sol(c))