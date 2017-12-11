#coding=utf-8
#装饰器执行顺序：
def test(func):
    print("------1--------")
    def wrap():
        print("-------inner1-------")
        func()
        print("-------inner2-------")
    print("--------2-----------")
    return wrap

@test
def f1():
    print("hello world")

f1()

# ------1--------
# --------2-----------
# -------inner1-------
# hello world
# -------inner2-------