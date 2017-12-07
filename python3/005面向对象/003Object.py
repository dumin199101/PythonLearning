#_*_coding:utf-8_*_
#多态：定义时对象不确定，运行时对象才确定下来。 类比Java Dog  d = new SmallDog() 跟 SamllDog sd = new SmallDog()
class Base(object):
    def info(self,temp):
        temp.test()

class Dog(Base):
    def test(self):
        print("i am Dog")

class SmallDog(Dog):
    def test(self):
        print("i am small Dog")



dog = Dog()
sd = SmallDog()

dog.info(dog)
sd.info(sd)