""" for i in range(12, 6, -1): #是<6，不<=6；range(start, stop, step)
    print(i, end=" ") """

""" n = int(input())
ans = 0
for i in range(n): #range(0, n, 1) 可以簡寫成range(n)
    temp = int(input())
    ans += temp
print(ans) """

num = int(input())
ans = 0
for i in range(1, num+1, 1):
    if i < num:
        print(i, end="+")
    else:
        print(i, end="=")
    ans += i
print(ans)