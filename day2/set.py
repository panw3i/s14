list_1 = [1,3,4,5,1,4,7,8,9]
list_1 = set(list_1)

print(list_1,type(list_1))


# 集合是无序的,所以元素没有对应的index,当然也不能切片
# print(list_1[0])

list_2 = [6,4,2,2,4,5,6,6,1]

list_2 = set(list_2)


# 交集
print(list_1.intersection(list_2))
print(list_1 & list_2)

# 并集(合并序列后去重复)
print(list_1.union(list_2))
print(list_1 | list_2)

# 差集
print(list_1.difference(list_2))
print(list_1 - list_2)  # list1里面有list2里面没有的

# 子集
print(list_1.issubset(list_2))
print(list_1.issuperset(list_2))


# 对称差集
print(list_1 ^ list_2) #不会同时存在左右两边的集合里

list_1.add(9)

list_1.remove(9)

list_1.update([9,0])

print(list_1)

print(len(list_1))

print(9 in list_1)

print(8 not in  list_1)


# 删除任意一个元素
print( list_1.pop())
print( list_1.pop())
print( list_1.pop())
print( list_1.pop())
print( list_1.pop())

print(list_1.remove(90))
print(list_1.discard(90))