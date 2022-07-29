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
x = 0
while x <= 10:
    x += 1
    if x == 3:
        break
    print(x)