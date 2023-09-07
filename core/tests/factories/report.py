from datetime import datetime
import factory.fuzzy
from core.models import Report


class ReportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Report

    start_date = '2023-03-23 20:00:00'
    end_date = '2023-03-25 20:00:00'
