from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import generics
from ..models import *
from ..serializers import *

class ReportDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs["pk"]
        report = Report.objects.get(id=id)
        serializer = ReportSerializer(instance=report)
        return Response(serializer.data)


class ReportCreateAPIVew(CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportListAPIVew(ListAPIView):
    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(
            instance=reports,
            many=True
        )
        data = serializer.data
        return Response(data)
