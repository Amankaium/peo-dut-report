from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import Transport
from .models import GSM




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
