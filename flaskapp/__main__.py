import os

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from flaskapp.application import app

if __name__ == '__main__':

    # Tornado HTTP Server
    devaddr=app.config['LISTEN']
    devport=int(app.config['PORT'])

    tornado = HTTPServer(WSGIContainer(app))
    tornado.listen(port=devport, address=devaddr)
    print(" * Tornado running on http://%s:%d" % (devaddr, devport))
    IOLoop.instance().start()

    # Built-in Flask HTTP Server
    #app.run(host=app.config['LISTEN'],
    #        port=int(app.config['PORT']),
    #        debug=app.config['DEBUG'])
