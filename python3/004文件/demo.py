#_*_coding:utf-8_*_
#python中先找局部变量，局部变量没有再找全局变量，如果对变量进行修改，如果有局部变量就修改局部变量，如果想对全局变量进行修改
#加global关键字
wendu = 0
def getwendu():
    wendu = 100

def printwendu():
    print("wendu是%s:"% wendu)

getwendu()
printwendu()