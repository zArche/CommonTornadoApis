#encoding:utf-8

from apis.hello import HelloHandler
from apis.getTime import GetTimeHandler
from apis.user import LoginHandler,RegisterHandler,UserDeatilHandler


handlers = [
    (r"/hello",HelloHandler),
    (r"/gettime",GetTimeHandler),
    (r"/login",LoginHandler),
    (r"/register",RegisterHandler),
    (r"/getUserDetail",UserDeatilHandler),
]