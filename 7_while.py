""" i = 0
while i < 6:
    print(i)
    i += 1 """

# while + break
""" i = 0
while True:
    x = input()
    if x == 'Q':
        break
    print(x) """

# break V.S. continue
""" x = 0
while x <= 10:
    x += 1
    if x == 3:
        break # 直接跳出整個回圈
    print(x) """

x = 0
while x <= 10:
    x += 1
    if x == 3:
        continue  # 終止以下的所有程式碼，直接進行下一個迴圈
    print(x)