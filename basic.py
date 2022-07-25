#Pass by reference
x = 3
y = x
print('id(x)', id(x))
print('id(y)', id(y))
print('=================================')
x = x + 1
print('x=', x)
print('y=', y)
print('id(x)', id(x))
print('id(y)', id(y))
print('=================================')

