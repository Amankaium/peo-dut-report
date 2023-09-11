from django.views import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import generics
from ..models import *
from ..serializers import *

class CardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardDetailAPIView(RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardListView(View):
    def get(self, request):
        context = {}
        context["cards"] = Card.objects.all()
        return render(request, 'core/cards.html', context)
