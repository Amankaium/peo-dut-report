from core.models import *
from .factories import DeltaReportFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class DeltaReportAPITestCase(APITestCase):
    def setUp(self):
        object_1 = DeltaReport()
        object_2 = DeltaReport()
        object_3 = DeltaReport()

    def test_create_delta_report(self):
        delta_report_data = DeltaReportFactory.build()

        url = reverse("/api/delta-reports/")
        response = self.client.post(url, delta_report_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(DeltaReport.objects.count(), 3)

