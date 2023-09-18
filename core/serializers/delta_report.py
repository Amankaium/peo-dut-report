from rest_framework import serializers
from core.models import *

class DeltaReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeltaReport
        fields = '__all__'
