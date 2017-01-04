from decimal import Decimal

from flask import url_for

from .factories import TrackerFactory


def test_home(client):
    response = client.get(url_for('core.home'))
    assert response.status_code == 200
    assert 'Welcome' in str(response.data)


def test_new(client, db):
    response = client.get(url_for('core.new'))
    assert response.status_code == 200
    response = client.post(
        url_for('core.new'),
        data=dict(name='test', email='test@test.com'),
        follow_redirects=False
    )
    assert response.status_code == 302
    assert 'tracker' in response.location


def test_tracker(client):
    tracker = TrackerFactory.create()
    response = client.get(url_for('core.tracker', guid=tracker.guid))
    assert response.status_code == 200
    response = client.get(url_for('core.tracker', guid='invalid'))
    assert response.status_code == 404


def test_new_measurement(client, db):
    tracker = TrackerFactory.create()
    response = client.get(url_for('core.new_measurement', guid=tracker.guid))
    assert response.status_code == 200
    response = client.post(
        url_for('core.new_measurement', guid=tracker.guid),
        data=dict(measured_on='2017-1-1', pounds='99'),
        follow_redirects=False
    )
    assert response.status_code == 302
    assert 'tracker' in response.location
    assert len(tracker.measurements.all()) == 1
    response = client.get(url_for('core.new_measurement', guid='invalid'))
    assert response.status_code == 404
