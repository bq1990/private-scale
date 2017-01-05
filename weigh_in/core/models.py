from datetime import date, datetime, timedelta

from ..database import db


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def last_weight(self):
        if self.entries.all():
            return self.entries[0].pounds

    def next_date(self):
        if self.entries.all():
            return self.entries[0].measured_on + timedelta(days=1)
        else:
            return date.today()

    def __repr__(self):
        return '{}'.format(self.name)


class Entry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    measured_on = db.Column(db.Date, default=date.today())
    pounds = db.Column(db.Numeric, nullable=False)
    log_id = db.Column(
        db.Integer, db.ForeignKey('log.id'), nullable=False)
    log = db.relationship(
        'Log',
        backref=db.backref('entries', lazy='dynamic')
    )

    __mapper_args__ = {
        'order_by': 'measured_on desc'
    }

    def __repr__(self):
        return '{}'.format(datetime.strftime(self.measured_on, '%Y-%m-%d'))

db.Index(
    'entry_unique_dt',
    Entry.log_id,
    Entry.measured_on, unique=True
)
