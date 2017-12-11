#coding=utf-8
#传递参数：
def test(func):
    print("------1--------")
    def wrap(*args,**kw):
        print("-------inner1-------")
        func(*args,**kw)
        print("-------inner2-------")
    print("--------2-----------")
    return wrap

@test
def f1(a,b):
    print("hello world,a=%d,b=%d"%(a,b))

@test
def f2(a,b,c):
    print("hello world,a=%d,b=%d,c=%d"%(a,b,c))

f1(1,2)
f2(11,22,33)

