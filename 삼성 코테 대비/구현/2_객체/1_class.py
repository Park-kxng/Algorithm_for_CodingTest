class code_007:
    def __init__(self, code, point, time):
        self.c = code
        self.p = point
        self.t = time

c , p, t = input().split()
code1  = code_007(c,p,t)
print("secret code : ",c)
print("meeting point : ",p)
print("time : ",t)