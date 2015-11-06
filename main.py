#encoding:utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import urls
import os


from tornado.options import define,options

define("port",default=8000,help="run on the given port",type=int)

cookie_secret_key = "RDdCMzZERTI2MzAwNzg4NjVFNjE3QUUxQTREMEFDMzc=" #base64(md5(Name+salt)) salt=birthday


handlers = urls.handlers  #接口地址

settings = {
    #"template_path" : os.path.join(os.path.dirname(__file__), "templates"),
    #"static_path" : os.path.join(os.path.dirname(__file__), "static"),
    "xsrf_cookies" : True,
    "cookie_secret": cookie_secret_key
}


if __name__ == "__main__":
    
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers,**settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    