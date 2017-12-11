#coding=utf-8
#两个装饰器同时使用：执行顺序由下向上执行
def makeBold(func):
    def wrap():
        return "<b>"+func()+"</b>"
    return wrap

def makeItalic(func):
    def wrap():
        return "<i>"+func()+"</i>"
    return wrap

@makeBold
@makeItalic
def test():
    return "Hello World"

ret = test()
print(ret)