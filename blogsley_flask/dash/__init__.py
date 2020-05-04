from flask import Blueprint

import __blogsley__

bp = Blueprint('dash', __name__, template_folder=f"{__blogsley__.static_folder}/dash")

from .routes import *
