""" for i in range(3):
    for j in range(2):
        print(i, j) """

n = int(input())
for i in range(n):
    for k in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()

# matrix
matrix = [[32, 57, 89], 
          [50, 20, 66], 
          [66, 78, 82], 
          [32, 89, 100], 
          [70, 100, 30]]
row = len(matrix)
