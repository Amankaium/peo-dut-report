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



class ReportListAPIView(APIView):
    def get(self, request):
        reports = Report.objects.all()
        serializer = ReportSerializer(
            instance=reports,
            many=True
        )
        data = serializer.data
        return Response(data)


class ReportDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs["pk"]
        report_object = Report.objects.get(id=id)
        serializer = ReportSerializer(instance=report_object)
        return Response(serializer.data)





