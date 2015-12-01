#encoding:utf-8

import json
import hashlib
import base64

'''
定义一个工具类，将常用的方法提取到该类
'''

class Utils():
    
    @staticmethod
    def dict2json(dic):
        return json.dumps(dic)
    
    @staticmethod
    def json2dic(js):
        return json.loads(js)
    
    @staticmethod
    def md5(str):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    
    @staticmethod
    def base64(str):
        return base64.b64encode(str)


if __name__ == "__main__":
    print Utils.base64(Utils.md5('arche'))
    
    
    