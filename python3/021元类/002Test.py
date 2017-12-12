#coding=utf-8
#利用元类重新定义类:python2中用__metaclass__,python3中用参数
def upper_attr(className,parentsTuple,attrDicts):
    newAttrDicts = {}
    for key,value in attrDicts.items():
        if not key.startswith("__"):
            newAttrDicts[key.upper()] = value
    return type(className,parentsTuple,newAttrDicts)

class Test(object,metaclass=upper_attr):
    name = "dudu"
    addr = "beijing"

t = Test()
print(hasattr(t,'NAME'))
print(hasattr(t,'ADDR'))
print(t.NAME)