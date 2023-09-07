from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import generics
from core.models import *
from core.serializers import *


class ReportAPIVew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportUpdateAPIVew(APIView):
    def put(self, request, *args, **kwargs):
        report_object = Report.objects.get(pk=kwargs["pk"])
        serializer = ReportSerializer(instance=report_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 202)
        return Response(serializer.errors, 400)


class ReportDeleteAPIVew(APIView):
    def delete(self, request, *args, **kwargs):
        report_object = Report.objects.get(pk=kwargs["pk"])
        report_object.delete()
        return Response("Successfully deleted", 204)


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


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

