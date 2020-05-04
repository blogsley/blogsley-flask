from flask import redirect, url_for

from blogsley_flask.root import bp

@bp.route('/')
def index():
    return redirect(url_for('admin.index'))
