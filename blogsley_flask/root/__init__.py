from flask import Blueprint

import __blogsley__

bp = Blueprint('root', __name__, template_folder=__blogsley__.static_folder)

from .routes import *
