from flask import Blueprint

import __blogsley__
bp = Blueprint('admin', __name__, template_folder=f"{__blogsley__.static_folder}")

from .routes import *
