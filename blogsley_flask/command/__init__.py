import os
import click
from loguru import logger

from flask import Flask
from flask.cli import FlaskGroup, pass_script_info

import flask_migrate

import __blogsley__

import blogsley_flask.pywsgi

@click.group(cls=FlaskGroup)
@click.option('--port', default=5000)
@pass_script_info
def cli(info, port):
    port = os.environ.get("BLOGSLEY_PORT") or port
    info.data = { 'port': port }
    os.environ['FLASK_RUN_PORT'] = str(port)
    os.environ["FLASK_RUN_FROM_CLI"] = "false"

@cli.command()
@click.pass_context
def init(ctx):
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
    #logger.debug(f"ctx.obj: {vars(ctx.obj)}")
    port = info.data['port']
    blogsley_flask.pywsgi.run(app, port)

@cli.command()
@click.pass_context
def dev(ctx):
    app = ctx.obj._loaded_app
    os.environ["FLASK_ENV"] = "debug"
    __blogsley__.debug = app.debug = True
    logger.debug(f"ctx.obj: {vars(ctx.obj)}")
    port = ctx.obj.data['port']
    blogsley_flask.pywsgi.run(app, port)

@cli.command()
@click.pass_context
def populate(ctx):
    from blogsley_flask.command.populate import populate as do_populate
    logger.debug(f"ctx.obj: {vars(ctx.obj)}")
    do_populate()
