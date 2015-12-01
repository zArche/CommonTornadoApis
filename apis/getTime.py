#encoding:utf-8

import time
import BaseHandler

TIMEFORMAT = '%Y-%m-%d %X'

class GetTimeHandler(BaseHandler.BaseHandler):
    def get(self):
        self.write(time.strftime(TIMEFORMAT,time.localtime()))
        