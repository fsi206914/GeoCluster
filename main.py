import os
import tornado.ioloop
import tornado.web
import ajax


application = tornado.web.Application([
    (r"/", tornado.web.RedirectHandler, {"url": "/static/frontend.html"}),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
    (r"/ajax/hvcnext", ajax.HVCNextHandler),
])


if __name__ == "__main__":

    t = ajax.ThreadClass()
    t.start()
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
