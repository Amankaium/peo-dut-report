from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import generics
from ..models import *
from ..serializers import *

class FuelTypeListAPIView(ListAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class FuelTypeCreateAPIView(generics.ListCreateAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class FuelTypeDetailAPIView(RetrieveAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer