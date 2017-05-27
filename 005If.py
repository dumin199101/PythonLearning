#coding=utf-8
#if条件分支
age = 10
print 'you age is:',age
if age>18:
    print 'adult'
elif age>10 and age<=18:
    print 'child'
else:
    print 'kid'
#for in 遍历
T = ['A','B','C','D']
for x in T:
    print x
#计算高斯问题:range(101)函数生成0-100之间的序列
sum = 0
for x in range(101):
    sum += x
print sum
#while循环
i = 100
sum = 0
while i>0:
    sum+=i
    i=i-1
print sum
#对raw_input输入数据类型转化:int()函数
birth = int(raw_input('birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'