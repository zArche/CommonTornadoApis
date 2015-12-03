#coding:utf-8
import tornado.web
import sys
sys.path.append("..")

import common.dao as dao
import json

########################################################################
class BaseHandler(tornado.web.RequestHandler):
    
    def initialize(self):
        try:
            self.session = dao.DBSession()
            self.dic = None #接口返回数据字典
            self.token = ""     #接口token值
        except:
            self.dic = {"error":1,
                   "reason":"database init error"}
            
  
    def on_finish(self):
        self.session.close()
        self.token = ""
        self.dic = None
     
    #@property
    #def session(self):
        #return self.session
    
    #@property
    #def token(self):
        #return self.token
     
    #@property
    #def dic(self):
        #return dic
    
    #----------------------------------------------------------------------
    def response(self): #返回请求结果
        ret = json.dumps(self.dic)
        self.write(ret)
        
    