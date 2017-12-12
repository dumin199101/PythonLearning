#coding=utf-8
#利用type函数创建元类：type("类名","继承父类元组","属性字典")
#实例对象 类 元类
class Test(object):
    def printNum(self,num):
        print("num is %d"%num)

t = Test()
t.printNum(10)

def printNumber(self):
    print("number is %d"%self.nums)
Test2 = type("Test2",(),{"printNumber":printNumber,"nums":100})
t2 = Test2()
t2.printNumber()