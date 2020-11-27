import flask_graphql
from flask import Response, request

from loguru import logger

from __blogsley__ import iam

class GraphQLView(flask_graphql.GraphQLView):
        def dispatch_request(self):
            iam.attach(request)
            return super().dispatch_request()
