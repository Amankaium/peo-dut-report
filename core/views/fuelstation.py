from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import generics
from ..models import *
from ..serializers import *

class FuelStationsListAPIView(APIView):
    def get(self, request):
        fuel_stations = Station.objects.all()
        serializer = StationSerializer(instance=fuel_stations, many=True)
        data = serializer.data
        return Response(data)

class FuelStationsDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs["pk"]
        fuel_stations_object = Station.objects.get(id=id)
        serializer = StationSerializer(instance=fuel_stations_object)
        return Response(serializer.data)