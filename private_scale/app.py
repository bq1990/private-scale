from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from . import core
from .settings import prod

debug_toolbar = DebugToolbarExtension()


def create_app(config=prod):
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)
    app.config.from_object(config)

    # from yourapplication.model import db
    # db.init_app(app)

    app.register_blueprint(core.views.blueprint)
    debug_toolbar.init_app(app)
    return app

app = create_app(prod)
