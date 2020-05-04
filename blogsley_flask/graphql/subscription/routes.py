import os
import sys
import json
from loguru import logger

from graphql_ws.gevent import GeventSubscriptionServer

from blogsley_flask.schema import schema
from blogsley_flask.graphql.subscription import bp

#Graphql Subscription Server
subscription_server = GeventSubscriptionServer(schema)

@bp.route('/graphql/')
def echo_socket(ws):
    logger.info('graphql websocket created')
    subscription_server.handle(ws)
    return []
