#coding=utf-8
#next(),__next__(),send()方法,send方法跟__next__()方法的区别就是可以传值过来,但必须以send(None)开启，否则报错
def createNum(m):
    n = 0
    a,b = 0,1
    while n<m:
        temp = yield b
        print(temp)
        a,b = b,a+b
        n = n+1

a = createNum(5)
print(a.__next__())
print(next(a))
print(a.send("haha"))

# 1
# None
# 1
# haha
# 2