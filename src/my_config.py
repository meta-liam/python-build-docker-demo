#!/usr/bin/env python
# coding: utf-8

import os
import json

health = {"config": {}, "models": {}}
data ={ "auth_list":[]}
isInit = False

def getenv(key_name, default=''):
    r = os.getenv(key_name)
    if r is None:
        return default
    return r

def get_health():
    return health

def get_auth_list():
    v = "[{'admin': '123'}, {'user1': '123'}]"
    txt = getenv("CHECK_AUTH", v)
    txt = txt.replace("'", "\"")
    # print(txt)
    return json.loads(txt)

def get_all_env():
    global isInit
    if isInit:
        return
    #return _get_product_env() # 生产的
    _get_dev_env() # 本地开发的
    isInit =True

def _get_dev_env():
    data["http_port"] = getenv("HTTP_PORT","5001")
    data["http_path"] = getenv("HTTP_PATH","/api/v1/")
    data["auth_list"] = get_auth_list()
    data["mysql_host"] = getenv("MYSQL_HOST","localhost")
    data["mysql_user"] = getenv("MYSQL_USER","root")
    data["mysql_port"] = getenv("MYSQL_PORT","3306")
    data["mysql_password"] = getenv("MYSQL_PWD","1234qwer")
    data["mysql_database"] = getenv("MYSQL_DB_NAME","test")

def _get_product_env():
    data["http_port"] = getenv("HTTP_PORT","5001")
    data["http_path"] = getenv("HTTP_PATH","/api/v1/")
    data["auth_list"] = get_auth_list()
    data["mysql_host"] = getenv("MYSQL_HOST","localhost") 
    data["mysql_user"] = getenv("MYSQL_USER","root")
    data["mysql_port"] = getenv("MYSQL_PORT","3306")
    data["mysql_password"] = getenv("MYSQL_PWD","123***")
    data["mysql_database"] = getenv("MYSQL_DB_NAME","test")