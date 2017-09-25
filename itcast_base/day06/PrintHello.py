#coding=utf-8
def printHello():
    "打印Hello"
    print "Hello"
printHello()

def sum(a,b):
    print a+b
sum(b=200,a=100)

#全局变量
num = 100
def test():
    # 如果修改全局变量，加global关键字声明，为了安全性
    global num
    #全局变量可以直接获取
    print num
    num+=2
    print num
test()