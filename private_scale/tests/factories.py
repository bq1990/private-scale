import uuid

import factory

from ..database import db
from ..core.models import Tracker


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
