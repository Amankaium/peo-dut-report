from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import generics
from ..models import *
from ..serializers import *

class OperationCreateTypeListAPIView(generics.ListCreateAPIView):
    queryset = OperationType.objects.all()
    serializer_class = OperationTypeSerializer

class OperationTypeDetailAPIView(RetrieveAPIView):
    queryset = OperationType.objects.all()
    serializer_class = OperationTypeSerializer