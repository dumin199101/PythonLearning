#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#Mysql数据库连接：
import mysql.connector
conn = mysql.connector.connect(host='localhost',port=3306,user='root',password='',database='test')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
rowcount = cursor.rowcount
print(rowcount)
#提交事务：
conn.commit()
cursor.close()
#运行查询：
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)


