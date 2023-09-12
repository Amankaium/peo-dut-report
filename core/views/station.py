from rest_framework.viewsets import ModelViewSet
from core.models import Station
from core.serializers import *
from django.views import View
from django.shortcuts import render

class StationViewSet(ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class StationListView(View):
    def get(self, request):
        context = {}
        context['stations'] = Station.objects.all()
        return render(request, 'core/station.html', context)


