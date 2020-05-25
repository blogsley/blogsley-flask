import os
import click
from loguru import logger

from flask import Flask
from flask.cli import FlaskGroup

import flask_migrate

import __blogsley__

import blogsley_flask.pywsgi

@click.group(cls=FlaskGroup)
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    os.environ["FLASK_RUN_FROM_CLI"] = "false"
    #os.environ["FLASK_APP"] = "blogsley_flask:create_app"
    #os.environ["FLASK_APP"] = "blogsley_flask"

@cli.command()
@click.pass_context
def init(ctx):
    flask_migrate.init()
    flask_migrate.migrate()
    flask_migrate.upgrade()
    do_populate()

@cli.command()
@click.pass_context
def run(ctx):
    app = ctx.obj._loaded_app
    os.environ["FLASK_ENV"] = "production"
    logger.debug(f"ctx.obj: {vars(ctx.obj)}")
    #ctx.obj._loaded_app.run()
    blogsley_flask.pywsgi.run(app)

@cli.command()
@click.pass_context
def dev(ctx):
    app = ctx.obj._loaded_app
    #os.environ["FLASK_ENV"] = "development"
    os.environ["FLASK_ENV"] = "debug"
    __blogsley__.debug = app.debug = True
    logger.debug(f"ctx.obj: {vars(ctx.obj)}")
    #ctx.obj._loaded_app.run(debug=True)
    blogsley_flask.pywsgi.run(app)

@cli.command()
@click.pass_context
def populate(ctx):
    from blogsley_flask.command.populate import populate as do_populate
    logger.debug(f"ctx.obj: {vars(ctx.obj)}")
    do_populate()
