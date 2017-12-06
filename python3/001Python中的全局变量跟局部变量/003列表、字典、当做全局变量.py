#_*_coding:utf-8_*_
#列表、字典做全局变量不用加global
list = [11,22,33]
dict = {"name":"good","age":22}
def getinfo():
    list.append(44)
    dict["addr"] = "beijing"
def printinfo():
    print(list)
    print(dict)
getinfo()
printinfo()