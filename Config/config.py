#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 15:07
# @Author  : wangxingwei
# @Site    : 
# @File    : Config.py
# @Software: PyCharm
import os
from Config.env import Env
env_path = os.path.join(os.path.abspath('./..') , 'env.ini')

Env(env_path)


CONFIG = {
    'api_id': Env.get('api_id',),
    'api_key': Env.get('api_key',),
    'api_secret': Env.get('api_secret',),
}
