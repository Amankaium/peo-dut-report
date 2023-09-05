from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from rest_framework import generics

from .serializers import *
from .models import *


class TransportListAPIView(APIView):
    def get(self, request):
        transports = Transport.objects.all()
        serializer = TransportSerializer(
            instance=transports,
            many=True
        )
        data = serializer.data
        return Response(data)


class TransportDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs["pk"]
        transport_object = Transport.objects.get(id=id)
        serializer = TransportSerializer(instance=transport_object)
        return Response(serializer.data)


class TransportCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = TransportSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"message": "Успешно создано"},
                status=201,
            )
        
        return Response(
            data=serializer.errors,
            status=400
        )

      
class ReportListAPIVew(APIView):
    def get(self, request):
        report = Report.objects.all()
        serializer = ReportSerializer(
            instance=report,
            many=True
        )
        data = serializer.data
        return Response(data)

     
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


class ReportDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs["pk"]
        report = Report.objects.get(id=id)
        serializer = ReportSerializer(instance=report)
        return Response(serializer.data)


class ReportCreateAPIVew(CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


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


class StationCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = StationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Успешно создано"}, status=201)

        return Response(data=serializer.errors, status=400)


class StationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class CardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class FuelTypeListAPIView(ListAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class OperationTypeListAPIView(ListAPIView):
    queryset = OperationType.objects.all()
    serializer_class = OperationTypeSerializer


class OperationTypeDetailAPIView(RetrieveAPIView):
    queryset = OperationType.objects.all()
    serializer_class = OperationTypeSerializer


class FuelTypeDetailAPIView(RetrieveAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class CardDetailAPIView(RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


