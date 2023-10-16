from django.views import View
from django.shortcuts import render, redirect
from core.models import MonthReport


class Home(View):
    def get(self, request):
        month_reports = MonthReport.objects.all()
        if month_reports:
            id = month_reports.last().id
            return redirect('delta-reports-update', id=id)
        return redirect('delta-reports-add')
