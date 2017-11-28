#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#序列化:dump,反序列化:load
import pickle
d = {"name":"dumin","age":22,"addr":"beijing"}
serialize = pickle.dumps(d)
print(serialize)
f = open('io_4.txt','wb')
pickle.dump(d,f)

f = open('io_4.txt','rb')
d = pickle.load(f)
f.close()
print(d)
