class user:
    def __init__(self, name = "codetree", lv = 10):
        self.n = name
        self.l = lv
name, lv = input().split()

user1 = user()
user2 = user(name,lv)

print("user",user1.n,"lv",user1.l)
print("user",user2.n,"lv",user2.l)