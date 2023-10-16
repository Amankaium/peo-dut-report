from django.views import View
from django.shortcuts import render, redirect
from core.models import MonthReport


class Home(View):
    def get(self, request):
        id = MonthReport.objects.order_by('year', 'month').last().id
        return redirect('delta-reports-update', id=id)
