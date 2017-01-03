from ..database import db


class Tracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String(80))
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __repr__(self):
        return '{}'.format(self.name)
