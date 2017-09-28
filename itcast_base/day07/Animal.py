#coding=utf-8
#定义一个类
class Animal:
    def run(self):
        print "动物都会跑步".decode("utf-8")

    def sleep(self):
        print "动物都要睡觉".decode("utf-8")

animal = Animal()
#设置属性
animal.color = "red"
animal.age = 10

#调用：
print animal.color
print animal.age
animal.run()
animal.sleep()