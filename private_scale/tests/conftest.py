import pytest

from private_scale.app import create_app
from private_scale.settings import test


@pytest.yield_fixture(scope='module')
def app():
    _app = create_app(test)
    ctx = _app.test_request_context()
    ctx.push()
    yield _app

    ctx.pop()
