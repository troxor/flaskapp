from __future__ import absolute_import
import os

from flaskapp.application import app

app.run(host=app.config['LISTEN'],
        port=app.config['PORT'],
        debug=app.config['DEBUG'])
