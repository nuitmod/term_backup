#!/usr/bin/env python

import tornado.ioloop
import tornado.web
import redis
import time, datetime

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Ruth")

class VoidHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("it is void")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/i_void", VoidHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server is wait on port 8888")
    tornado.ioloop.IOLoop.current().start()
