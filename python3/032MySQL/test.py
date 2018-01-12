# coding=utf-8
# 测试数据库操作类
from MySQLHelper import MySQLHelper
def main():
    helper =  MySQLHelper('127.0.0.1','root','','pymysql')
    helper.connect()

    # 添加
    helper.cud(sql='insert into `tb_stu`(`name`) values(%s)',params=["mary"])

    # 查询
    results = helper.query(sql="select * from `tb_stu`")
    for result in results:
        id = result[0]
        name = result[1]
        print("id:%s,name:%s"%(id,name))

    # 关闭
    helper.close()


if __name__ == '__main__':
    main()