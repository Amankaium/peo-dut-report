from datetime import datetime
import factory
from core.models import CardOperation
from .card import CardFactory


class CardOperationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CardOperation

    date = factory.fuzzy.FuzzyDateTime(datetime(2020, 1, 1))
    station = factory.SubFactory(CardFactory)
    sum_som = 100
    