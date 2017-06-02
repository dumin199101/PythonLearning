#coding=utf-8
'面向对象高级'
__author__= 'lieyan123091'
from types import MethodType
class Student(object):
    __slots__ = ('name', 'age','score','set_age')  # 用tuple定义允许绑定的属性名称
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print "Score Info:Name:%s,Score:%s"%(self.name,self.score)

bart = Student('Bart Simpson', 59)
bart.print_score()
#手动更改属性值
bart.name = 'du'
bart.print_score()
#给一个实例绑定的方法，对另一个实例是不起作用的
def set_age(self,age):
    self.age = age
bart.set_age = MethodType(set_age,bart,Student) #给实例绑定一个方法
bart.set_age(33)
print bart.age
#给所有的实例绑定方法
Student.set_age = MethodType(set_age, None, Student)
lisa = Student('Lisa Simpson', 87)
lisa.set_age(12)
print lisa.age

#使用__slots__限制class属性,定义的属性仅对当前类起作用，对继承的子类是不起作用的
# lisa.addr = 'bj'
# print lisa.addr

