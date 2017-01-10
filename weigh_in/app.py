import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from . import core
from . import filters
from .database import db
from .settings import common

debug_toolbar = DebugToolbarExtension()


def create_app(config=common):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(core.views.blueprint)
    app.register_blueprint(filters.blueprint)
    db.init_app(app)
    debug_toolbar.init_app(app)
    if os.getenv('FORCE_SSL'):
        from flask_sslify import SSLify
        SSLify(app)
    return app

