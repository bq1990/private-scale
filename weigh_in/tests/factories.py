from datetime import date, timedelta

import factory

from ..database import db
from ..core.models import Entry, Log


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class LogFactory(BaseFactory):
    name = factory.Sequence(lambda n: 'myname-{0}'.format(n))
    guid = factory.Sequence(lambda n: 'guid-{0}'.format(n))

    class Meta:
        model = Log


class EntryFactory(BaseFactory):
    measured_on = factory.Sequence(lambda n: date.today() + timedelta(days=n))
    pounds = factory.Sequence(lambda n: 150 - n)

    class Meta:
        model = Entry
