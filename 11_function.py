# 參數 parameter & 引數 argument

#引數分為位置引數和關鍵字引數
""" def add_numbers(num1, num2):
    print(num1 + num2)
#位置引數
add_numbers(3, 9)
add_numbers(num2=9, num1=3) """

# local 區域 V.S. global 全域。
""" 在函式內的變數，函式外無法讀取
在函式外的變數，函式內可以讀 """

#import
import random # import整個random package
# import random as r # import整個random package然後命名為r
# from random import randint, shuffle # 只import randint和shuffle兩個function
n = int(input())
ans = [random.randint(1, 1100) for i in range(n)]
print(ans)