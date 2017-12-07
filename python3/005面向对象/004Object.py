#_*_coding:utf-8
#类属性(静态变量)，实例属性（成员变量），类方法(cls)，实例方法(self)，静态方法(跟类实例无关)
class Game(object):
    #类属性
    num = 0
    #实例方法
    def __init__(self,name):
        #实例属性
        self.__name = name
    #类方法：
    @classmethod
    def changeNum(cls):
        cls.num = 100
    #静态方法：
    @staticmethod
    def log():
        print("-----------------")
        print("Hello World")
        print("-----------------")
#调用：
game = Game("cyhx")
Game.changeNum()
print(Game.num)
print(game.num)
Game.log()
game.log()