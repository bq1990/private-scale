import pytest

from private_scale.app import create_app


@pytest.yield_fixture(scope='module')
def app():
    _app = create_app()
    ctx = _app.test_request_context()
    ctx.push()
    yield _app

    ctx.pop()
