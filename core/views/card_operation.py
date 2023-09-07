from core.serializers import *
from core.models import CardOperation
from rest_framework.viewsets import ModelViewSet

class CardOperationViewSet(ModelViewSet):
    queryset = CardOperation.objects.all()
    serializer_class = CardOperationSerializer