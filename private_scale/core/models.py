from datetime import date, datetime, timedelta

from ..database import db


class Tracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def last_weight(self):
        if self.measurements.all():
            return self.measurements[0].pounds

    def next_date(self):
        if self.measurements.all():
            return self.measurements[0].measured_on + timedelta(days=1)
        else:
            return date.today()

    def __repr__(self):
        return '{}'.format(self.name)


class Measurement(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    measured_on = db.Column(db.Date, default=date.today())
    pounds = db.Column(db.Numeric, nullable=False)
    tracker_id = db.Column(
        db.Integer, db.ForeignKey('tracker.id'), nullable=False)
    tracker = db.relationship(
        'Tracker',
        backref=db.backref('measurements', lazy='dynamic')
    )

    __mapper_args__ = {
        'order_by': 'measured_on desc'
    }

    def __repr__(self):
        return '{}'.format(datetime.strftime(self.measured_on, '%Y-%m-%d'))

db.Index(
    'measurement_unique_dt',
    Measurement.tracker_id,
    Measurement.measured_on, unique=True
)

