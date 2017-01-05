import pytest

from weigh_in.app import create_app
from weigh_in.database import db as _db
from weigh_in.settings import test


@pytest.yield_fixture(scope='module')
def app():
    _app = create_app(test)
    ctx = _app.test_request_context()
    ctx.push()
    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='module')
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()

