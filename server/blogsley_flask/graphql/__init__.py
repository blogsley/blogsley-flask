from flask import Blueprint
from flask_cors import CORS

bp = Blueprint('graphql', __name__, template_folder='templates')
CORS(bp)

from blogsley_flask.graphql import routes
