# print(): 輸出的意思，預設是自動換行
print('Hello', end = ' ') #取消自動換行
print('Python', end = ',')
print('Nice')

# \: 跳脫字元
print('=================================')
print('Hello\nPython')

# 輸出格式: format
print('=================================')
guest = 'Jean'
host = 'AL'
print('Hello, ' + guest + '. My name is ' + host + '.')
#f-string
print(f'Hello, {guest}. My name is {host}.')
#format
print('Hello, {}. My name is {}.'.format(guest, host))

#取到小數點後第n位
print('=================================')
pi = 3.14159265
#f-string
print(f'Pi is {pi:.3f}')
#format
print('Pi is {:.4f}'.format(pi))