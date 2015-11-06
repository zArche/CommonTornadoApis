#encoding:utf-8

import tornado.web
import time


TIMEFORMAT = '%Y-%m-%d %X'

class GetTimeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(time.strftime(TIMEFORMAT,time.localtime()))
        