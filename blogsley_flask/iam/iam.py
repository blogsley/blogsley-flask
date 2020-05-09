from functools import wraps
from loguru import logger

from flask import current_app, _app_ctx_stack, g, request

from blogsley_flask.jwt import decode_auth_token
from .exceptions import AuthorizationException

class Identity:
    def __init__(self):
        self.user = None

    @classmethod
    def create(self, name):
        return roles[name]()

class Role(Identity):
    def __init__(self):
        super().__init__()

class Anonymous(Role):
    pass

class Reader(Anonymous):
    pass

class Author(Reader):
    pass

class Editor(Author):
    pass

class Moderator(Author):
    pass

class Admin(Moderator):
    pass

class IAM:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
        self.Identity = None

    def init_app(self, app):
        app.teardown_appcontext(self.teardown)
        @app.before_request
        def before_request():
                #logger.debug(f"request: {vars(request)}")
                token = decode_auth_token(request)
                logger.info(f"token: {token}")
                if not token:
                    identity = Anonymous()
                else:
                    identity = Identity.create(token['role'])
                g.identity = identity


    def teardown(self, exception):
        ctx = _app_ctx_stack.top

    def needs(self, role_name):
        role = roles[role_name]
        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                if not isinstance(g.identity, role):
                    raise AuthorizationException(f"needs role: {role_name}")
                return fn(*args, **kwargs)
            return wrapper
        return decorator
        
roles = {
    'Anonymous': Anonymous,
    'Reader': Reader,
    'Author': Author,
    'Editor': Editor,
    'Moderator': Moderator,
    'Admin': Admin
}