#encoding:utf-8

from apis.hello import HelloHandler
from apis.getTime import GetTimeHandler


handlers = [
    (r"/hello",HelloHandler),
    (r"/gettime",GetTimeHandler),
]