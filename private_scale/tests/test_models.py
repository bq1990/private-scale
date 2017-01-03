from datetime import date

from ..core.models import Measurement, Tracker


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
