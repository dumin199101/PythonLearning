#_*_coding=utf-8_*_
#匿名函数：
test = lambda x,y:x+y
result = test(1,2)
print("result is:1+2=%s"%str(result))

#匿名函数排序：
a = [23,4,123,1,432,421,643,21]
a.reverse()
print(a) #逆序
a.sort(reverse=True)
print(a) #从大到小排序

b = [
    {"name":"cc","age":22},
    {"name":"aa","age":26},
    {"name":"dd","age":28}
]
b.sort(key=lambda x:x['name'])
print(b)