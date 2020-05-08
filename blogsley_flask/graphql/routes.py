import os
import sys

from flask import render_template, request, current_app
from flask_graphql import GraphQLView
from graphql.backend import GraphQLCoreBackend

from blogsley_flask.graphql import bp
from blogsley_flask.schema import schema

#from blogsley_flask.graphql.view import GraphQLView

path = os.path.join(os.path.dirname(__file__), "templates/playground.html")
templateFile = open(path)
TEMPLATE = templateFile.read()

class CustomBackend(GraphQLCoreBackend):
    def __init__(self, executor=None):
        super().__init__(executor)
        self.execute_params['allow_subscriptions'] = True


#from .sentry import Sentry

bp.add_url_rule(
    '/graphql/',
    view_func=GraphQLView.as_view(
        'graphql',
        #backend=CustomBackend(),
        schema=schema,
        graphiql=True,
        graphiql_template=TEMPLATE,
        #subscriptions=True
        #middleware = [Sentry()]
    )
)