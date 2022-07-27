#Pass by reference
x = 3
y = x #x和y會指向相同的記憶體位置
print('id(x)', id(x))
print('id(y)', id(y))
print('=================================')
x = x + 1 #x和y會指向不同的記憶體位置
print('x=', x)
print('y=', y)
print('id(x)', id(x))
print('id(y)', id(y)) 
print('=================================')
z = 4 #x和z會指向不同的記憶體位置
print('id(z)', id(z))
"""python在處理的時候會先找value是否已存在，所以效能較慢"""

#輸出

