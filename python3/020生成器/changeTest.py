#coding=utf-8
#交换两个数：
#方式1
a = 10
b = 20
a,b = b,a
print("a=%d"%a)
print("b=%d"%b)
#方式2
c = 100
d = 200
c = c+d
d = c-d
c = c-d
print("c=%d"%c)
print("d=%d"%d)