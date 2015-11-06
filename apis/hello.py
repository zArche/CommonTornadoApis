#encoding:utf-8

import tornado.web

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name","world")
        self.write("[get]hello "+ name)
        
    def post(self):
        name = self.get_argument("name","world")
        self.write("[post]hello "+ name)        
        