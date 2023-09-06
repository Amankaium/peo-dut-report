from rest_framework.viewsets import ModelViewSet
from core.models import Station
from core.serializers import *


class StationViewSet(ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

