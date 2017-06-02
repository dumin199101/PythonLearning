#coding=utf-8
'05 Class 面向对象'
__author__ = 'lieyan123091'
class Worker:
    '''
      this is a test class
    '''
    #成员变量
    addr = "beijing"
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    def hello(self):
        'say hello function'
        print "Hello:",self.name,",Salary:",self.pay

    @classmethod
    def showAddr(cls):
        #装饰器函数，类方法，可以访问类成员
        print cls.addr


if __name__ == '__main__':
    worker = Worker('dudu',2200)
    worker.hello()
    print worker.addr
    print hasattr(worker,'addr')
    print setattr(worker,'addr','tianjin')
    print worker.addr
    print Worker.__name__
    print Worker.__doc__
    print Worker.__dict__
    print Worker.__module__
    Worker.showAddr()

