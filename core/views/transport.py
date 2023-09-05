from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import generics
from ..models import *
from ..serializers import *

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
