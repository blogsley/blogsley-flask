from flask import render_template, request, current_app
from blogsley.schema import schema
from blogsley.graphql.subscription import bp
import os
import sys

import json

from flask import Flask, make_response
from flask_sockets import Sockets

from graphql.backend import GraphQLCoreBackend

from graphql_ws.gevent import GeventSubscriptionServer
from geventwebsocket.handler import WebSocketHandler

from blogsley.schema import schema

from blogsley.graphql.subscription import routes

#Graphql Subscription Server
subscription_server = GeventSubscriptionServer(schema)
#app = current_app
#app.app_protocol = lambda environ_path_info: 'graphql-ws'


@bp.route('/graphql/')
def echo_socket(ws):
    print('graphql-ws')
    subscription_server.handle(ws)
    return []
