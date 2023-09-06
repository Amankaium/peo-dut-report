from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import generics
from core.models import *
from core.serializers import *


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