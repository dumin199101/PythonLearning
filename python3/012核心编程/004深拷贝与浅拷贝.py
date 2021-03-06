#coding=utf-8
#对比内存图理解
#对于copy函数：如果是可变类型：只做一次拷贝，如果是不可变类型：一次拷贝也不做
import copy
a = [1,2,3]
b = [4,5,6]
c = [a,b]
d = c
e = copy.copy(c)
#id的地址不同，但会同样会影响到值
print(id(c),c)
print(id(d),d)
print(id(e),e)

# 32610504 [[1, 2, 3], [4, 5, 6]]
# 32610504 [[1, 2, 3], [4, 5, 6]]
# 32610440 [[1, 2, 3], [4, 5, 6]]


print("*************")
a.append(4)
print(id(c),c)
print(id(d),d)
print(id(e),e)

# 32610504 [[1, 2, 3, 4], [4, 5, 6]]
# 32610504 [[1, 2, 3, 4], [4, 5, 6]]
# 32610440 [[1, 2, 3, 4], [4, 5, 6]]

print("-"*100)
a = [1,2,3]
b = [4,5,6]
c = (a,b)
d = c
e = copy.copy(c)
#id的地址相同，会同样会影响到值
print(id(c),c)
print(id(d),d)
print(id(e),e)

# 32177416 ([1, 2, 3], [4, 5, 6])
# 32177416 ([1, 2, 3], [4, 5, 6])
# 32177416 ([1, 2, 3], [4, 5, 6])

print("*************")
a.append(4)
print(id(c),c)
print(id(d),d)
print(id(e),e)

# 32177416 ([1, 2, 3, 4], [4, 5, 6])
# 32177416 ([1, 2, 3, 4], [4, 5, 6])
# 32177416 ([1, 2, 3, 4], [4, 5, 6])