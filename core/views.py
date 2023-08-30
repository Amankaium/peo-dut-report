from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *




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

class DriverListAPIView(APIView):
    def get(self, request):
        drivers = DriversName.objects.all()
        serializer = DriverSerializer(
            instance=drivers,
            many=True
        )
        data = serializer.data
        return Response(data)
    
class ReportDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs["pk"]
        report = Report.objects.get(id=id)
        serializer = ReportSerializer(instance=report)
        return Response(serializer.data)


class FuelStationsListAPIView(APIView):
    def get(self, request):
        fuel_stations = GSM.objects.all()
        serializer = GSMSerializer(instance=fuel_stations, many=True)
        data = serializer.data
        return Response(data)

class FuelStationsDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs["pk"]
        fuel_stations_object = GSM.objects.get(id=id)
        serializer = GSMSerializer(instance=fuel_stations_object)
        return Response(serializer.data)
