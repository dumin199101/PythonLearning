# coding=utf-8
__author__ = '1766266374@qq.com'
# 封装MYSQL数据库操作类

from pymysql import *

class MySQLHelper(object):
    """
    Python操作MySQL数据库类库封装
    """
    def __init__(self,host,user,password,database,port=3306,charset='utf8'):
        """
        参数初始化
        :param host:
        :param user:
        :param password:
        :param database:
        :param port:
        :param charset:
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
        self.conn = self.cursor = None

    def connect(self):
        """
        数据库连接&初始化cursor对象
        :return:
        """
        self.conn = connect(host=self.host,user=self.user,password=self.password,database=self.database,port=self.port,charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        """
        释放资源
        :return:
        """
        self.cursor.close()
        self.conn.close()

    def cud(self,sql,params=[]):
        """
        增删改操作
        :param sql:
        :param params:
        :return:
        """
        try:
            self.cursor.execute(sql,params)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def query(self,sql,params=[]):
        """
        查询操作
        :param sql:
        :param params:
        :return:
        """
        try:
            self.cursor.execute(sql,params)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
