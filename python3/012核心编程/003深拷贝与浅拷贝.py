#coding=utf-8
#对比内存图理解
#深拷贝：会像递归一样做深层次拷贝，id的地址不同，不会影响到值
import copy
a = [1,2,3]
b = [4,5,6]
c = [a,b]
d = c
e = copy.deepcopy(c)
#值都是1,2,3,4,5,6 但是e的id不同于cd
print(id(c),c)
print(id(d),d)
print(id(e),e)

# 36018248 [[1, 2, 3], [4, 5, 6]]
# 36018248 [[1, 2, 3], [4, 5, 6]]
# 36018184 [[1, 2, 3], [4, 5, 6]]

print("*************")
a.append(4)
print(id(c),c)
print(id(d),d)
print(id(e),e)

# 42375304 [[1, 2, 3, 4], [4, 5, 6]]
# 42375304 [[1, 2, 3, 4], [4, 5, 6]]
# 42375240 [[1, 2, 3], [4, 5, 6]]

print("-"*100)
a = [1,2,3]
b = [4,5,6]
c = (a,b)
d = c
e = copy.deepcopy(c)
print(id(c),c)
print(id(d),d)
print(id(e),e)

# 31653064 ([1, 2, 3], [4, 5, 6])
# 31653064 ([1, 2, 3], [4, 5, 6])
# 31207880 ([1, 2, 3], [4, 5, 6])

print("*************")
a.append(4)
print(id(c),c)
print(id(d),d)
print(id(e),e)

# 35650952 ([1, 2, 3, 4], [4, 5, 6])
# 35650952 ([1, 2, 3, 4], [4, 5, 6])
# 35650440 ([1, 2, 3], [4, 5, 6])
