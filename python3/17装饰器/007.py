#coding=utf-8
#装饰器带参数：
def testing(info):
    def test(func):
        def wrap():
            func()
            print("info:%s"%info)
        return wrap
    return test

@testing("hello python")
def f1():
    print("hello world")

f1()

