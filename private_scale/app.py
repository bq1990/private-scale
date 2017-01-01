from flask import Flask

from . import core
from .settings import prod


def create_app(config=prod):
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)
    app.config.from_object(config)

    # from yourapplication.model import db
    # db.init_app(app)

    app.register_blueprint(core.views.blueprint)

    return app

app = create_app(prod)
