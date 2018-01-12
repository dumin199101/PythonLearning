# coding=utf-8
# Mysql与Python交互
from pymysql import *
try:
    # 连接
    conn = connect(host='127.0.0.1',port=3306,user='root',password='',database='pymysql',charset='utf8')
    # 创建cursor对象
    cursor = conn.cursor()
    sql = 'select * from `tb_stu`'
    # 执行SQL
    cursor.execute(sql)
    #获取查询结果：
    # fetchall()
    # results = cursor.fetchall()
    # for result in results:
    #     id = result[0]
    #     name = result[1]
    #     print("Student Info:id is %s,name is %s"%(id,name))
    # fetchone()
    # id,name = cursor.fetchone()
    # print("Student Info:id is %s,name is %s" % (id, name))
    # fetchmany(n):返回前n行
    results = cursor.fetchmany(2)
    for result in results:
        id = result[0]
        name = result[1]
        print("Student Info:id is %s,name is %s"%(id,name))
    # 打印记录数
    print(cursor.rowcount)
    # 关闭连接
    cursor.close()
    conn.close()
except Exception as e:
    print(e)