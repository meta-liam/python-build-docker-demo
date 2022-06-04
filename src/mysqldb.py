# -*- coding:utf-8 -*-
import pymysql

class MySql(object):
    def __init__(self,host="localhost",user="root",password="",database="db",port=3306,charset="utf8"): 
        self.host=host 
        self.port=port
        self.user=user 
        self.password=password 
        self.charset=charset
        self.database = database
        self.conn = None

    def get_version(self):
        return "1.0.0"

    def connect(self):
        if (self.conn):
            return
        self.conn = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             database=self.database,
                             port=self.port,
                             cursorclass=pymysql.cursors.DictCursor)
    
    def query(self,sql):
        cur = self.conn.cursor()      #获取对应的操作游标
        cur.execute(sql)
        data = cur.fetchall()
        #cur.close()
        #self.conn.commit()
        return data

    def execute(self,sql):
        cur = self.conn.cursor()      #获取对应的操作游标
        cur.execute(sql)
        self.conn.commit()
    
    def insert(self,sql,values= None):
        cur = self.conn.cursor()      #获取对应的操作游标
        if (values):
            cur.execute(sql,values)
        else:    
            cur.execute(sql)
        #self.conn.commit() 外面可以连续插入多个才commit

    def close(self):
        self.conn.close()
        self.conn = None


if __name__ == '__main__':
    cursor = MySql(password="1234qwer",database="test")
    cursor.connect()
    # delete
    sql2 = "delete from `users` WHERE `id` = 1 "
    cursor.execute(sql2)
    # # insert
    sql3 = "INSERT INTO `users` (`email`, `password`) VALUES ('xxx@qq.com', '123456')"
    cursor.execute(sql3)
    #  # select
    sql1 = "SELECT `id`, `password`,`email` FROM `users` WHERE `id` > 0"
    data = cursor.query(sql1)
    print(data)

    cursor.close()


# python mysqldb.py
