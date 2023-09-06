import factory
from core.models import *


class CardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Card

    id_realcom = factory.Sequence(lambda n: n)
    number = factory.Sequence(lambda k: k)