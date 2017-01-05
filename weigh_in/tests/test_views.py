from flask import url_for

from .factories import EntryFactory, LogFactory


def test_home(client):
    response = client.get(url_for('core.home'))
    assert response.status_code == 200
    assert 'Welcome' in str(response.data)


def test_new_log(client, db):
    response = client.get(url_for('core.new_log'))
    assert response.status_code == 200
    response = client.post(
        url_for('core.new_log'),
        data=dict(name='test', email='test@test.com'),
        follow_redirects=False
    )
    assert response.status_code == 302
    assert 'log' in response.location


def test_log_detail(client):
    log = LogFactory.create()
    response = client.get(url_for('core.log_detail', guid=log.guid))
    assert response.status_code == 200
    response = client.get(url_for('core.log_detail', guid='invalid'))
    assert response.status_code == 404


def test_new_entry(client, db):
    log = LogFactory.create()
    response = client.get(url_for('core.new_entry', guid=log.guid))
    assert response.status_code == 200
    response = client.post(
        url_for('core.new_entry', guid=log.guid),
        data=dict(measured_on='2017-1-1', pounds='99'),
        follow_redirects=False
    )
    assert response.status_code == 302
    assert 'log' in response.location
    assert len(log.entries.all()) == 1
    response = client.get(url_for('core.new_entry', guid='invalid'))
    assert response.status_code == 404


def test_delete_entry(client, db):
    log = LogFactory.create()
    entry = EntryFactory(log=log)
    assert len(log.entries.all()) == 1
    response = client.get(
        url_for('core.delete_entry', guid=log.guid, entry_date=entry.measured_on)
    )
    assert response.status_code == 200
    response = client.post(
        url_for('core.delete_entry', guid=log.guid, entry_date=entry.measured_on),
        follow_redirects=False
    )
    assert response.status_code == 302
    assert len(log.entries.all()) == 0
    response = client.get(
        url_for('core.delete_entry', guid='invalid', entry_date='2000-1-1')
    )
    assert response.status_code == 404
    response = client.get(
        url_for('core.delete_entry', guid=log.guid, entry_date='2000-1-1')
    )
    assert response.status_code == 404
