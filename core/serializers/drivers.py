from rest_framework import serializers
from core.models import *


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriversName
        fields = '__all__'