from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transport
from .serializers import TransportSerializer


class TransportAPIView(APIView):
    def get(self, request):
        transports = Transport.objects.all()
        serializer = TransportSerializer(
            instance=transports,
            many=True
        )
        data = serializer.data
        return Response(data)
