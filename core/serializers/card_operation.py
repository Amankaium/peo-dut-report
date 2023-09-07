from rest_framework import serializers
from core.models import *

class CardOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardOperation
        fields = '__all__'
