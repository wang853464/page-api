# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 15:14
# @Author  : wangxingwei
# @Site    : 
# @File    : env.py
# @Software: PyCharm
import configparser


class Env(object):
    # 实例句柄
    _instance = None
    # 文件操作句柄
    _handler = None

    def __new__(cls, file):
        # 再__init__构造函数之前
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._handler = configparser.ConfigParser()
            cls._handler.read(file)
        return cls._instance

    @staticmethod
    def get(param, default=None):
        if Env._handler is None:
            return default
        else:
            params = param.split('.')
            if len(params) == 2:
                if Env._handler.has_section(params[0]) and Env._handler.has_option(params[0], params[1]):
                    return Env._handler.get(params[0], params[1])
                else:
                    return default
            else:
                return default
