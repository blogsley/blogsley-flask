import os
import sys

from loguru import logger

from flask import Flask, current_app

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from flask_mail import Mail
from flask_babel import Babel, lazy_gettext as _l

import jinja2

import blogsley_flask.config
from blogsley_flask.config import Config
from blogsley_flask.db import create_db

class BlogsleyFlask(Flask):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    @classmethod
    def create(self, config=None, environment=None):
        share_folder = blogsley_flask.config.share_folder
        db_folder = blogsley_flask.config.db_folder
        static_folder = blogsley_flask.config.static_folder
        logger.info(f"static_folder: {static_folder}")

        static_url_path = ''

        blogsley_flask.config.app = app = BlogsleyFlask(self.__name__, static_url_path=static_url_path, static_folder=static_folder)
        app.config.from_object(Config)

        blogsley_flask.config.db = db = SQLAlchemy(app)
        blogsley_flask.config.migrate = migrate = Migrate(app, db)

        blogsley_flask.config.login = login = LoginManager(app)
        login.login_view = 'auth.login'
        login.login_message = 'Please log in to access this page.'

        blogsley_flask.config.mail = mail = Mail(app)
        blogsley_flask.config.babel = babel = Babel(app)

        from blogsley_flask.auth import bp as auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')

        from blogsley_flask.image import bp as image_bp
        app.register_blueprint(image_bp, url_prefix='/images')

        from blogsley_flask.root import bp as root_bp
        app.register_blueprint(root_bp)

        from blogsley_flask.graphql import bp as graphql_bp
        app.register_blueprint(graphql_bp)

        app.app_protocol = lambda environ_path_info: 'graphql-ws'
        from blogsley_flask.sockets import Sockets
        sockets = Sockets(app)
        from blogsley_flask.graphql.subscription import bp as ws
        sockets.register_blueprint(ws, url_prefix=r'/')

        return app

def create_app(config=None, environment=None):
    logger.info(f"config : {config}")
    logger.info(f"environment: {environment}")

    app = BlogsleyFlask.create(config, environment)

    #Configure Jinja2
    my_loader = jinja2.ChoiceLoader([
            app.jinja_loader,
            jinja2.FileSystemLoader(['blogsley_flask/templates']),
        ])
    app.jinja_loader = my_loader

    #Configure Login
    from blogsley_flask.user import User
    @blogsley_flask.config.login.user_loader
    def load_user(id):
        return User.query.get(int(id))
        
    return app
    