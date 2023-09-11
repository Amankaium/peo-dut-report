from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import generics
from ..models import *
from django.views import View
from django.shortcuts import render
from ..serializers import *


class GetFuelTypeView(View):
    template_name = 'core/get_fuel_type.html'
    def get(self, request):
        context = {}
        context['fuel_types'] = FuelType.objects.all()
        return render(request, self.template_name, context)


class FuelTypeListAPIView(ListAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class FuelTypeCreateAPIView(generics.ListCreateAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class FuelTypeDetailAPIView(RetrieveAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer