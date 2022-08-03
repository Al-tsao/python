""" for i in range(3):
    for j in range(2):
        print(i, j) """

""" n = int(input())
for i in range(n):
    for k in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print() """

# matrix
""" matrix = [[32, 57, 89], 
          [50, 20, 66], 
          [66, 78, 82], 
          [32, 89, 100], 
          [70, 100, 30]]
row = len(matrix)
col = len(matrix[0])
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=", ")
    print() """
    
matrix = [[32, 57, 89], 
          [50, 20, 66], 
          [66, 78, 82], 
          [32, 89, 100], 
          [70, 100, 30]]
row = len(matrix)
col = len(matrix[0])
row_sum = [0 for i in range(row)]
col_sum = [0 for j in range(col)]
for i in range(row):
    for j in range(col):
        row_sum[i] += matrix[i][j]
        col_sum[j] += matrix[i][j]
print(row_sum)
print(col_sum)