from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import tornado.options

from flaskapp.application import app

tr = WSGIContainer(app)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = HTTPServer(tr)
    http_server.listen(int(app.config['PORT']))
    IOLoop.instance().start()
