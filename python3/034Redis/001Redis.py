# coding=utf-8
# Redis跟Python交互
from redis import *
client = StrictRedis(host='192.168.226.128',port=6379)
pipe = client.pipeline()
pipe.set("name","huahua")
pipe.set("age",22)
pipe.execute()
name = client.get("name")
print(name.decode("utf-8"))