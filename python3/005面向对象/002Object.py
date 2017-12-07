#_*_coding:utf-8_*_
#多继承同名方法的调用顺序：类名.__mro__(method resolution order)
class Base(object):
    def test(self):
        print("Base")

class A(Base):
    def test(self):
        print("A")

class B(Base):
    def test(self):
        print("N")

class C(A,B):
    # def test(self):
    #     print("C")
    pass

c = C()
c.test()
print(C.__mro__)