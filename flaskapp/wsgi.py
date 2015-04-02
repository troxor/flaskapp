from __future__ import absolute_import

from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
import tornado.options

from flaskapp.application import app

if __name__ == '__main__':
    print 'Please use a WSGI Server. module=flaskapp.wsgi, callable=app'
    exit(1)
