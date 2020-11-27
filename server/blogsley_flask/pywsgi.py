import os
from loguru import logger

from gevent import monkey
monkey.patch_all()

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

# https://coderwall.com/p/q2mrbw/gevent-with-debug-support-for-flask

from werkzeug.serving import run_with_reloader
from werkzeug.debug import DebuggedApplication

# If using PyCharm enable Gevent debugging support under:
#   Settings->Build, Execution, Deployment->Python Debugger

#TODO:Web sockets problem with debug:
'''
WebSocket connection to 'ws://localhost:8000/subscriptions' failed: Error during WebSocket handshake:
Sent non-empty 'Sec-WebSocket-Protocol' header but no response was received
'''
def run_server(app, port):
    server = pywsgi.WSGIServer(('0.0.0.0', port), app, handler_class=WebSocketHandler)
    server.serve_forever()

def debug_server(app, port):
    server = pywsgi.WSGIServer(('0.0.0.0', port), DebuggedApplication(app), handler_class=WebSocketHandler)
    server.serve_forever()

def run(app, port):
    if app.debug:
        logger.info('blogsley running in debug mode')
        def debugfn():
            debug_server(app, port)
        run_with_reloader(debugfn)
    else:
        run_server(app, port)

if __name__ == "__main__":
    run(app)