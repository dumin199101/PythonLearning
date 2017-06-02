#coding=utf-8
'''
06 Python Module
  eg:
    import demo : demo.Parent.showInfo()
    from demo import Parent,Child : Parent.showInfo()
    from demo import *
'''
#访问局部变量跟全局变量
sum = 200
def info():
    s = 100
    print globals()
    print locals()
info()
