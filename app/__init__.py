import os
import socket

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

from redis import Redis

app = Flask(__name__)

redishost = os.getenv('REDISHOST')
redisport = os.getenv('REDISPORT')

redis = Redis(host=redishost, port=redisport)

app.config.from_object('config')
app.config.from_envvar('FLASKAPP_SETTINGS', silent=True)


@app.route('/')
def show_index():
    hostname = socket.gethostname()
    site_hostname = os.environ['SITE_HOSTNAME']
    return render_template('home.html', **locals())

@app.route('/about')
def show_about():
    hostname = socket.gethostname()
    site_hostname = os.environ['SITE_HOSTNAME']
    return render_template('about.html', **locals())

@app.route('/contact')
def show_contact():
    hostname = socket.gethostname()
    site_hostname = os.environ['SITE_HOSTNAME']
    return render_template('contact.html', **locals())

@app.route('/redistest')
def show_redistest():
    redis.incr('hits')
    return 'Redis OK! It has been tested %s times.' % redis.get('hits')

@app.route('/test')
def show_test():
    page = []
    page.append( str(request.view_args) )
    page.append( str(request.headers) )
    page.append( str(request.environ) )
    page = page + dir(request)
    return "<br /><br/>".join(page)

@app.route('/status')
def show_status():
    return "OK"

if __name__ == '__main__':
    print("hello")
    app.run(debug=True, host='0.0.0.0', port=8000)
