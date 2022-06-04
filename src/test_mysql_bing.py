import unittest
import logging
import os
from mysqldb import *
import time
import my_config

# https://pypi.org/project/PyMySQL/
# 类：https://zhuanlan.zhihu.com/p/30024792
# 参考：https://www.jianshu.com/p/0507583ec41f

class TestMySqlMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_mysql1(self):
        print('info 信息')
        cursor = MySql()
        print("version:",cursor.get_version())

    def test_mysql_all(self):
        my_config.get_all_env()
        cursor = MySql(host=my_config.data["mysql_host"],user=my_config.data["mysql_user"],password=my_config.data["mysql_password"],database=my_config.data["mysql_database"])
        cursor.connect()
        save_time = int( time.time())
        print(save_time)
        
        #  select
        sql1 = "SELECT * FROM `ads_bing_location_report` WHERE `id` = 1"
        data = cursor.query(sql1)
        print(data)

        cursor.close()
        

if __name__ == '__main__':
    unittest.main()

# cd test
# python test_mysql_bing.py