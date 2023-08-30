from rest_framework import serializers
from .models import *


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriversName
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class GSMSerializer(serializers.ModelSerializer):
    class Meta:
        model = GSM
        fields = '__all__'
