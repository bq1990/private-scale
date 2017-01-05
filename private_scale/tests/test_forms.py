from ..core.forms import LogForm


def test_trackerform(client):
    form = LogForm(csrf_enabled=False)
    assert form.validate() is False

    form = LogForm(csrf_enabled=False, name='test', email='test@test.com')
    assert form.validate() is True