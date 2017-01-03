import uuid
from datetime import date, timedelta

import factory

from ..database import db
from ..core.models import Measurement, Tracker


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class TrackerFactory(BaseFactory):
    name = factory.Sequence(lambda n: 'myname-{0}'.format(n))
    email = factory.Sequence(lambda n: 'email-{0}@example.com'.format(n))
    guid = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'anon weight'))

    class Meta:
        model = Tracker


class MeasurementFactory(BaseFactory):
    measure_on = factory.Sequence(lambda n: date.today() + timedelta(days=n))
    pounds = factory.Sequence(lambda n: 150 - n)

    class Meta:
        model = Measurement
