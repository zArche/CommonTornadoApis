#coding:utf-8
import tornado.web
import sys
sys.path.append("..")

import common.dao as dao

########################################################################
class BaseHandler(tornado.web.RequestHandler):
    
    def initialize(self):
        self.session = dao.DBSession()
        self.token = ""        

    def on_finish(self):
        self.session.close()
        self.token = ""
        
     
        
    
    