
from flask import Flask

from delivery.ext import cli, config, db, site, toolbar


def create_app():
    """Factory Principal"""
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    db.init_app(app)
    cli.init_app(app)


    return app
