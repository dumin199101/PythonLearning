#coding=utf-8
#类装饰器
class Test(object):
    def __init__(self,func):
        print("---初始化---")
        self.__func = func
    def __call__(self, *args, **kwargs):
        print("----装饰----")
        self.__func()

@Test
def test():
    print("Hello World")

test()