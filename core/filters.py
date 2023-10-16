import django_filters
from .models import DeltaReport


class DeltaReportFilter(django_filters.FilterSet):
    class Meta:
        model = DeltaReport
        fields = ['month_report']
