#coding=utf-8
#列表生成式
#后边代表循环的次数，前边代表变量的值
a = [i for i in range(0,10)]
print(a)
#元组方式
b = [(x,y) for x in range(0,2) for y in range(0,4)]
print(b)
#加入筛选条件
c = [i for i in range(10) if i%2==0]
print(c)