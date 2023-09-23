from rest_framework import serializers
from core.models import *

class DeltaReportSerializer(serializers.Serializer):
    class Meta:
        model = DeltaReport
        fields = '__all__'