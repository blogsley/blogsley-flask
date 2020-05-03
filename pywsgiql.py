import json

from flask import Flask, make_response
from flask_graphql import GraphQLView
from flask_sockets import Sockets

from graphql_ws.gevent import GeventSubscriptionServer


from app import create_app
app = create_app()
sockets = Sockets(app)

#TODO: This has to be import after the app is created.  Smelly
from blogsley_flask.schema import schema

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()