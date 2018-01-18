# coding=utf-8
# MongoDB与Python交互
from pymongo import *
client = MongoClient("mongodb://admin:123@localhost:27017/admin")
# 选择数据库
db = client.py
# 选择集合
stu = db.stu
# 插入测试
# stu.insert({"name":"wanghaiyan","age":22})

# 查询
cursors = stu.find()
for cursor in cursors:
    print(cursor['name'],cursor['age'])