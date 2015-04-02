from __future__ import print_function

import os
import socket

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from redis import Redis

app = Flask(__name__)

# Default values come from config.py
app.config.from_object('flaskapp.config') # some defaults
#app.config.from_envvar('FLASKAPP_SETTINGS', silent=True)

# Merge OS environment into app.config, overriding config.py
# This might end up being a dumb idea, we'll see
for i in os.environ:
    app.config[i] = os.environ[i]

if 'REDISHOST' in app.config:
    redishost = app.config['REDISHOST']

if 'REDISPORT' in app.config:
    redisport = app.config['REDISPORT'] or 6379

if app.config['DEBUG']:
    print(app.config)

redis = Redis(host=redishost, port=redisport)


@app.route('/')
def show_index():
    hostname = socket.gethostname()
    site_hostname = app.config['SITE_HOSTNAME']
    return render_template('home.html', **locals())

@app.route('/about')
def show_about():
    hostname = socket.gethostname()
    site_hostname = app.config['SITE_HOSTNAME']
    return render_template('about.html', **locals())

@app.route('/contact')
def show_contact():
    hostname = socket.gethostname()
    site_hostname = app.config['SITE_HOSTNAME']
    return render_template('contact.html', **locals())

@app.route('/test')
def show_test():
    page = []
    page.append( str(request.view_args)+"<hr />" )
    page.append( str(request.headers)+"<hr />"   )
    page.append( str(request.environ)+"<hr />"   )

    try:
        redis.incr('testhits')
        page.append('Redis OK!, tested %s times!' % redis.get('testhits'))
    except:
        page.append('Redis FAIL')
    page.append("<hr />")

    page = page + dir(request)
    return "<br /><br/>".join(page)
