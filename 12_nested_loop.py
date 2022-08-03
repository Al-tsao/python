for i in range(3):
    for j in range(2):
        print(i, j)

#30:06

n = int(input())
for i in range(n):
    for k in range(n - i - 1):
        print(" ", end="")
    for j in rnage(i + 1):
        print("*", end="")
    print()