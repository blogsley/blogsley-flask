import os
import click
from loguru import logger

from flask import Flask
from flask.cli import FlaskGroup, pass_script_info

import flask_migrate

import __blogsley__

import blogsley_flask.pywsgi

@click.group(cls=FlaskGroup)
@click.option('--port', default=8000)
@pass_script_info
def cli(info, port):
    port = os.environ.get("BLOGSLEY_PORT") or port
    info.data = { 'port': port }
    os.environ['FLASK_RUN_PORT'] = str(port)
    os.environ["FLASK_RUN_FROM_CLI"] = "false"

@cli.command()
@pass_script_info
def init(info):
    flask_migrate.init()
    flask_migrate.migrate()
    flask_migrate.upgrade()
    from blogsley_flask.command.populate import populate as do_populate
    do_populate()

@cli.command()
@pass_script_info
def run(info):
    app = info._loaded_app
    os.environ["FLASK_ENV"] = "production"
    port = int(os.environ.get("PORT", info.data['port']))
    blogsley_flask.pywsgi.run(app, port)

@cli.command()
@pass_script_info
def dev(info):
    app = info._loaded_app
    os.environ["FLASK_ENV"] = "debug"
    __blogsley__.debug = app.debug = True
    port = int(os.environ.get("PORT", info.data['port']))
    blogsley_flask.pywsgi.run(app, port)

@cli.command()
@pass_script_info
def populate(info):
    from blogsley_flask.command.populate import populate as do_populate
    do_populate()
