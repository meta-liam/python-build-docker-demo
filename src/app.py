#!/usr/bin/env python
# coding: utf-8

import sys
import my_config as my_config

sys.path.append('./')

from my_router import Router

def run_http():
    my_config.get_all_env()
    print(my_config.data)
    _pre = my_config.data["http_path"]
    port = int(my_config.data["http_port"])
    debug = False
    api = Router(_pre, port, debug)
    api.run()


if __name__ == '__main__':
    print("[INFO] app.py run_http")
    run_http()

# python app.py