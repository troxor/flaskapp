
import os
import socket

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

app.config.from_object('config')
app.config.from_envvar('FLASKAPP_SETTINGS', silent=True)

@app.route('/')
def show_index():
    hostname = socket.gethostname()
    return render_template('home.html', **locals())

@app.route('/about')
def show_about():
    hostname = socket.gethostname()
    return render_template('about.html', **locals())

@app.route('/contact')
def show_contact():
    hostname = socket.gethostname()
    return render_template('contact.html', **locals())

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
