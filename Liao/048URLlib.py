#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#模拟http请求：
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print("Status:",f.status,f.reason)
    for k,v in f.getheaders():
        print("%s:%s"%(k,v))
    print("Data:",data.decode("utf-8"))
