#coding=utf-8
#装饰器对有返回值的函数进行装饰：
def test(func):
    print("------1--------")
    def wrap():
        print("-------inner1-------")
        ret = func()
        print("-------inner2-------")
        return ret
    print("--------2-----------")
    return wrap

@test
def f1():
    print("hello world")
    return "haha"

ret = f1()
print("the return value is %s"%ret)
