#coding=utf-8
#is跟==的区别：注意数字的情况（待讨论）
a = [11,22,33]
b = [11,22,33]
c = a
print("a's id:%s"%id(a))
print("b's id:%s"%id(b))
print("c's id:%s"%id(c))

print(a==b) #True
print(a is b) #False
print(a==c) #True
print(a is c) #True

print("-"*100)
a = "abc"
b = "abc"
c = a

print("a's id:%s"%id(a))
print("b's id:%s"%id(b))
print("c's id:%s"%id(c))
print(a==b) #True
print(a is b) #True
print(a==c) #True
print(a is c) #True

print("-"*100)
a = 10000
b = 10000
c = a

print("a's id:%s"%id(a))
print("b's id:%s"%id(b))
print("c's id:%s"%id(c))
print(a==b) #True
print(a is b) #True
print(a==c) #True
print(a is c) #True