from django.views import View
from django.shortcuts import render
from core.models import *
import requests

class GetDriversListView(View):
    def get(self, request):
        context = {}
        context['drivers'] = DriversName.objects.all()
        return render(request, 'core/get_drivers.html', context)

