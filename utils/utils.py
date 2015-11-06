#encoding:utf-8

import json

'''
定义一个工具类，将常用的方法提取到该类
'''

class Utils(object):
    def __init__(self):
        pass
    
    def dict2json(dic):
        return json.dumps(dic)
    
    def json2dic(js):
        return json.loads(js)
    
    