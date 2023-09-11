from django.views import View
from django.shortcuts import render
from core.models import *
import requests


class GetTransportView(View):
    template_name = 'core/get_transports.html'
    def get(self, request):
        context = {}
        context['transports'] = Transport.objects.all()
        return render(request, self.template_name, context)