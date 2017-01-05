from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from . import core
from .database import db
from .settings import prod

debug_toolbar = DebugToolbarExtension()


def create_app(config=prod):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(core.views.blueprint)
    db.init_app(app)
    debug_toolbar.init_app(app)
    return app

app = create_app(prod)
