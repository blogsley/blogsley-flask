from flask import Blueprint, current_app
from flask_cors import CORS

bp = Blueprint('graphql-subscription', __name__)
CORS(bp)

from .routes import *