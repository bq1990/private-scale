from ..core.forms import TrackerForm


def test_trackerform(client):
    form = TrackerForm(csrf_enabled=False)
    assert form.validate() is False

    form = TrackerForm(csrf_enabled=False, name='test', email='test@test.com')
    assert form.validate() is True