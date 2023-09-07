import factory
from core.models import *

class StationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Station

    name = 'test station name'
    id_realcom = factory.Sequence(lambda n: f"{n}")
