#coding=utf-8
#类的实例化
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print "Score Info:Name%s,Score:%s"%(self.name,self.score)

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

#类的封装
class Student1(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print "Score Info:Name%s,Score:%s"%(self.__name,self.__score)

bart = Student1('Bart Simpson', 59)
lisa = Student1('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
bart._Student1__name #外部访问

print "#############继承跟多态################"
class Animal(object):

    def __init__(self,name):
        self.name = name

    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'

    def eat(self):
        print 'Eating meat...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

dog = Dog("huahua")
dog.run()
dog.eat()

cat = Cat("aaa")
cat.run()

#判断对象是否是类的实例
print isinstance(dog,Animal)

#获取对象的属性跟方法
print dir(dog)

#对对象的属性进行设置跟获取
print getattr(dog,'name')
print hasattr(dog,'name')
setattr(dog,'name','hehe')
print getattr(dog,'name')

