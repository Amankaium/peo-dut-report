import factory
from core.models import *


class TransportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transport
    
    mark = 'test mark 1'
    number = factory.Sequence(lambda n: f"TN {n}")
    trailer = factory.Sequence(lambda k: f"TNT {k}")
