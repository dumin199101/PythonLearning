#coding=utf-8
#生成器：解决一次性大数据量内存溢出问题，提供生成算法，使用时调用next方法生成，调用失败会抛出StopIteration异常
#生成器方式1：
g = (x*2 for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

