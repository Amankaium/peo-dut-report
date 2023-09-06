import factory
from core.models import *

class FuelTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FuelType

    fuel = "test fuel 1"
    id_realcom = factory.Sequence(lambda n: f"{n}")