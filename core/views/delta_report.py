from core.serializers import *
from core.models import DeltaReport
from rest_framework.viewsets import ModelViewSet


class DeltaReportViewSet(ModelViewSet):
    queryset = DeltaReport.objects.all()
    serializer_class = DeltaReportSerializer
