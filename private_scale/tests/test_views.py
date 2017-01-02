from flask import url_for


def test_home(client):
    response = client.get(url_for('core.home'))
    assert response.status_code == 200
    assert 'Welcome' in str(response.data)


def test_new(client):
    response = client.get(url_for('core.new'))
    assert response.status_code == 200


def test_tracker(client):
    response = client.get(url_for('core.tracker', guid='1234'))
    assert response.status_code == 200
