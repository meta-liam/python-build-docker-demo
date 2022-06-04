#!/usr/bin/env python
# coding: utf-8
import json

from flask import Flask
from flask import request
import my_config as my_config
import time
import my_work

app = Flask(__name__)

def after_request(resp):
    h = "Access-Control-Allow-Headers,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Cache-Control," \
        "Content-Type,Content-Length,Authorization,Accept,AppID,AppSecret,UserID,Utoken"
    resp.headers['Access-Control-Allow-Origin'] = "*"
    resp.headers['Access-Control-Allow-Methods'] = "POST,GET,OPTIONS,PUT,DELETE,PATCH,HEAD"
    resp.headers['Access-Control-Allow-Headers'] = h
    return resp


auth_list = [{"admin": "123"}, {"user1": "123"}]

def work_demo(db):
    return my_work.get_report_task(db)
    #return db

def check_auth(headers):
    app_id = headers.get('AppID')
    app_secret = headers.get('AppSecret')
    if {app_id: app_secret} in auth_list:
        # print("check_auth: True")
        return True
    else:
        # print("check_auth: False")
        return False

class Router(object):
    pre = '/'#'/ai-api/v1/nlp/'

    def __init__(self, pre_url='/ai-api/v1/', port=5000, debug=False):
        #print('[INFO] router.py init ')
        global pre, auth_list
        pre = pre_url
        # self.app = app #Flask(__name__)
        self.pre = pre_url
        self.port = port
        self.debug = debug
        # self.models = All()
        my_config.health["config"] = {"time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) }
        my_config.get_all_env()
        auth_list = my_config.data["auth_list"]
        #print("[INFO]  router.py auth_list: ",auth_list)
        #print("[INFO]  router.py auth_list: ",config.env_data)

        def return_json(v):
            return json.dumps(v, ensure_ascii=False), 200, {"Content-Type": "application/json"}

        @app.route('/')
        def index():
            return 'index'

        @app.route(pre + 'hello')
        def hello():
            return 'hello'

        @app.route(pre + 'health')
        def health():
            return my_config.get_health()

        @app.before_request
        def before_request():
            # print("resp:method=", request.method) # POST
            pass

        @app.route(pre + 'work_demo', methods=['OPTIONS'])
        def work_demo_options():
            return 'ok'

        @app.route(pre + 'work_demo_request', methods=['POST'])
        def work_demo_post():
            if not check_auth(request.headers):
                return return_json({'code': 110, 'inputs': {}, 'meg': 'no auth'})
            output_data =work_demo(request.json)
            #print('output_data:', output_data)
            return return_json(output_data)

        @app.errorhandler(404)
        def page_not_found(e):
            # note that we set the 404 status explicitly
            return '404'

    def run(self):
        print('[INFO] router.py run : pre-path:', self.pre, ' port:', self.port, ' debug:', self.debug)
        app.after_request(after_request)
        app.run(host='0.0.0.0', port=self.port, debug=self.debug)

# if __name__ == '__main__':
#     r = Router(pre_url = "/api/v1/",port=3012)
#     r.run()


# python router.py
'''
curl  http://localhost:3012/api/v1/health

curl -H 'AppID: user1' -H 'AppSecret: 123' -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"start": "2022-05-01", "stop":"2022-06-01"}'  http://localhost:3012/api/v1/work_demo

'''