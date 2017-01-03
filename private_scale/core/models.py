from datetime import date

from ..database import db


class Tracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __repr__(self):
        return '{}'.format(self.name)


class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    measured_on = db.Column(db.Date, default=date.today())
    pounds = db.Column(db.Integer, nullable=False)
    tracker_id = db.Column(
        db.Integer, db.ForeignKey('tracker.id'), nullable=False)
    tracker = db.relationship(
        'Tracker',
        backref=db.backref('measurements', lazy='dynamic')
    )

    def __repr__(self):
        return '{}'.format(self.id)
