import django_filters
from core.models import *


class TransportFilter(django_filters.FilterSet):
    class Meta:
        model = Transport
        fields = {
            'mark': ['icontains'],
            'number': ['icontains'],
            'trailer': ['icontains'],
            'id_realcom': ['exact'],
            'name_realcom': ['icontains'],
        }






