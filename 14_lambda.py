#匿名函數
""" def f(x):
    return x + 3
print(f(3))

add = lambda x: x+3
print(add(3))

print((lambda x: x+3)(3))
 """
#lambda的組合
#和filter
numbers = [3, 50, 2, 80, 49, 10, 6]
print(list(filter(lambda x: x > 10, numbers)))
#和map
scores = input().split()
map(lambda x: int(x), scores)