
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import socket

app = Flask(__name__)

app.config.from_object('config')

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

#class ChatWebSocket(tornado.websocket.WebSocketHandler):
#    clients = []
#    
#    def open(self):
#        ChatWebSocket.clients.append(self)
#
#    def on_message(self, message):
#        for client in ChatWebSocket.clients:
#            client.write_message(message)
#
#    def on_close(self):
#        ChatWebSocket.clients.remove(self)

#tornado_app = tornado.web.Application([
#    (r'/websocket', ChatWebSocket),
#    (r'.*', tornado.web.FallbackHandler, 
#        {'fallback': tornado.wsgi.WSGIContainer(app)})
#])

#tornado_app.listen(5000)
#tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    print("hello")
    app.run(debug=True, host='0.0.0.0', port=8000)
