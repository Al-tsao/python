#匿名函數
def f(x):
    return x + 3
print(f(3))

add = lambda x: x+3
print(add(3))

print((lambda x: x+3)(3))