from django.shortcuts import render
from django.views import View
from core.models import DeltaReport, Transport

class DeltaReportListView(View):
    def get(self, request):
        transport_id = request.GET.get('transport')
        date = request.GET.get('date')
        delta_reports = DeltaReport.objects.all()
        if transport_id:
            delta_reports = delta_reports.filter(transport_id=transport_id)
        if date:
            delta_reports = delta_reports.filter(date=date)
        transports = Transport.objects.all()
        context = {'delta_reports': delta_reports, 'transports': transports}
        return render(request, 'core/delta_report.html', context)
