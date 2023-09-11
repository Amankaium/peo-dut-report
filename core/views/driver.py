from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from core.serializers import *
from django.views import View
from django.shortcuts import render
from core.models import *


class GetDriversListView(View):
    def get(self, request):
        context = {}
        context['drivers'] = DriversName.objects.all()
        return render(request, 'core/get_drivers.html', context)


class DriverViewSet(ModelViewSet):
    queryset = DriversName.objects.all()
    serializer_class = DriverSerializer

class DriverListCreateAPIView(APIView):
    def get(self, request):
        drivers = DriversName.objects.all()
        serializer = DriverSerializer(
            instance=drivers,
            many=True
        )
        data = serializer.data
        return Response(data)
    
    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            new_driver = serializer.save()
            new_serializer = DriverSerializer(instance=new_driver)
            return Response(new_serializer.data, 201)
        
        return Response(serializer.errors, 400)


class DriverDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs["pk"]
        report = DriversName.objects.get(id=id)
        serializer = DriverSerializer(instance=report)
        return Response(serializer.data)