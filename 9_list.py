""" list = [1, 3, 5, 7, 9]
print(list[4])
print(len(list))
print(list[-1])
print(list[1:3]) # Slice 包頭不包尾
print(list[-1:-4]) # Slice 順序一定要從左到右，從右到左會沒東西
print(list[-3:]) #print(list[-1:-4])就是這個意思 """

# 串列 methods

#for + list
""" numbers = [3, 5, 6, 10, 2, 8]
for i in range(0, len(numbers), 1): # i: index
    print(numbers[i], end=" ")
print(" ")
for v in numbers: #v: value
    print(v, end=" ") """

# 列表推導式 list comprehension
ans = []
for i in range(10):
    ans.append(i)
#和下面的結果一樣，把for迴圈放到ans的[]中，又把ans.append(i)簡化成i
ans = [i for i in range(10)]
print(ans)
