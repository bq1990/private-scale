from flask import url_for


def test_home(client):
    response = client.get(url_for('core.home'))
    assert response.status_code == 200
    assert 'Welcome' in str(response.data)


def test_new(client):
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
    response = client.get(url_for('core.tracker', guid='1234'))
    assert response.status_code == 200
