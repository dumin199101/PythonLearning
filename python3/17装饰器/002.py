#coding=utf-8
#装饰器：本质：在没有改变原来函数定义的情况下，增加功能，符合开闭原则。
#定义一个闭包：
def test(func):
    def inner():
        print("权限验证")
        #执行原来的函数：
        func()
    return inner

@test
def f1():
    print("hello world")

@test
def f2():
    print("hello python")

#调用
f1()
f2()

