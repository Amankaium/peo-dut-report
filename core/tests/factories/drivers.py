import factory
from core.models import *

class DriversNameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DriversName

    full_name = 'test name'