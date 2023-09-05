from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from core.serializers import *


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer