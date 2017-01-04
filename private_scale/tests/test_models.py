from datetime import date, datetime

from ..core.models import Measurement, Tracker


def test_tracker(client, db):
    tracker = Tracker(
        name='test',
        email='test@test.com',
        guid='123'
    )
    assert str(tracker) == 'test'


def test_measurement(client, db):
    tracker = Tracker(
        name='test',
        email='test@test.com',
        guid='123'
    )
    measurement = Measurement(
        measured_on=date.today(),
        pounds=123,
        tracker=tracker
    )
    tracker.measurements.append(measurement)
    db.session.add(tracker)
    db.session.commit()
    assert measurement.id
    assert str(measurement) == datetime.strftime(
        measurement.measured_on, '%Y-%m-%d')

