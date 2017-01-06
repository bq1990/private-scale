from datetime import date

from ..core.forms import EntryForm, LogForm


def test_logform(client):
    form = LogForm(csrf_enabled=False, name='')
    assert form.validate() is False

    form = LogForm(csrf_enabled=False, name='test')
    assert form.validate() is True


def test_entryform(client):
    form = EntryForm(csrf_enabled=False)
    assert form.validate() is False

    form = EntryForm(csrf_enabled=False, measured_on=date.today, pounds=-1)
    assert form.validate() is False
    assert form.pounds.errors
