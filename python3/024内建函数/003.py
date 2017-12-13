#coding=utf-8
#偏函数：可以传递默认参数，以后调用不用传递了
from functools import partial,wraps
def show(*args,**kwargs):
    print(args)
    print(kwargs)

f1 = partial(show,1,2,3)
f1()
f1(4,5,6)
f1(name="dudu",age=22)

#wraps装饰：
def test(func):
    '''
    test函数
    :param func:
    :return:
    '''
    @wraps(func)
    def inner():
        '''
        inner函数
        :return:
        '''
        print("权限验证")
        #执行原来的函数：
        func()
    return inner

@test
def f1():
    '''
    f1函数
    :return:
    '''
    print("hello world")

print(help(f1))