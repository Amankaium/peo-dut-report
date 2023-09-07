from datetime import datetime, timezone
import factory
from core.models import CardOperation
from .station import StationFactory
from .card import CardFactory
from .fuel import FuelTypeFactory
from .operation import OperationTypeFactory



class CardOperationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CardOperation

    date = factory.fuzzy.FuzzyDateTime(datetime(2020, 1, 1, tzinfo=timezone.utc))
    station = factory.SubFactory(StationFactory)
    card = factory.SubFactory(CardFactory)
    fuel_type = factory.SubFactory(FuelTypeFactory)
    operation_type = factory.SubFactory(OperationTypeFactory)
    balance_before = 40
    balance_after = 50
    dose = 60
    price_som = 70
    sum_som = 100
