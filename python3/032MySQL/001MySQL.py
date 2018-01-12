# coding=utf-8
# Mysql与Python交互
from pymysql import *
try:
    # 连接
    conn = connect(host='127.0.0.1',port=3306,user='root',password='',database='pymysql',charset='utf8')
    # 创建cursor对象
    cursor = conn.cursor()
    sql = 'insert into `tb_stu`(`name`) values("henry")'
    # 执行SQL
    cursor.execute(sql)
    # 默认开启事务，提交
    conn.commit()
    # 关闭连接
    cursor.close()
    conn.close()
except Exception as e:
    print(e)