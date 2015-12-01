#encoding:utf-8

import BaseHandler

class HelloHandler(BaseHandler.BaseHandler):
    def get(self):
        name = self.get_argument("name","world")
        self.write("[get]hello "+ name)
        
    def post(self):
        name = self.get_argument("name","world")
        self.write("[post]hello "+ name)        
        