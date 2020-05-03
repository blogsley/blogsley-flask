from flask import Blueprint

import blogsley_flask.config

bp = Blueprint('root', __name__, template_folder=blogsley_flask.config.static_folder)

from .routes import *
