#coding=utf-8
#生成器Generator
g = (x * x for x in range(10))
for i in g:
    print i
print "###############"
def g(n):
    for i in range(n):
        yield i**2
for i in g(5):
    print i,":"