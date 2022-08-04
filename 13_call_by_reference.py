#變數和list有差別

#變數
num = 3
def change_number(number):
    number += 3
    print(f"def total: {id(number)}")
change_number(number = num)
print(f"main total: {id(num)}")
""" 在一開始number = num，num和number會指向同一位置，但是後來number變成6，所以會指向另為一個有6的位置 """

#list
""" 在list，如果函式內的list指向函數外的list，因為list是串接的關係，一旦函式內的list改變，全域的list也會變 """