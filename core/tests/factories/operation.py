import factory
from core.models import *

class OperationTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OperationType

    name = "test oper 1"
    id_realcom = factory.Sequence(lambda n: f"{n}")
