# 迴圈 + 字串轉型
x = input()
print(x.split())
list = []
for v in x.split():
    list.append(int(v))
print(list)