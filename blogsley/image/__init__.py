from flask import Blueprint
from flask_cors import CORS

bp = Blueprint('images', __name__)
CORS(bp)

from .entity import Image
from .routes import *
