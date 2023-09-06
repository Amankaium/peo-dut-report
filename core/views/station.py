from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Station
from core.serializers import *


class StationViewSet(ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

