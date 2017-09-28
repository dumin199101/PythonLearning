#coding=utf-8
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        str = "Object is Print!!!"
        return str

    def showInfo(self):
        print "Name is : %s ,Age is : %d!"%(self.name,self.age)

dog1 = Dog("huahua",2)
dog1.showInfo()
dog2 = Dog("mingming",3)
dog2.showInfo()

print(dog1)

