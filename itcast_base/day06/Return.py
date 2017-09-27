#coding=utf-8
def test():
    a = 100
    return a
    b = 200
    return b
    c = 300
    return c
result = test()
print result #100 一个函数中有多个return时，取最前面的return做返回值

def test2():
    name = "dumin"
    age = 22
    id = 10010
    #return name,age,id
    #return (name,age,id) #元组方式
    #return [name,age,id] #列表方式
    return {"name":name,"age":age,"id":id}

# name,age,id = test2()
# print name
# print age
# print id

info = test2()
print info["name"]
print info["age"]
print info["id"]

