import my_config as my_config
import my_utils

# 入口
def get_report_task(input_json):
    async_report_task()# 异步处理
    return input_json

@my_utils.my_async
def async_report_task(url =''):
    return "ok"

if __name__ == '__main__':
    rs = get_report_task({"start": "2022-04-01", "stop":"2022-04-15"})
    print(rs)

# python my_work.py
