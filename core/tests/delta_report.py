from rest_framework.test import APITestCase
from core.models import *
from .factories import DeltaReport

class DeltaReportAPITestCase(APITestCase):
    def setUp(self):
        object_1 = DeltaReport()
        object_2 = DeltaReport()
        object_3 = DeltaReport()

    def delta_report_list_view_with_filters(self):
        response = self.client.get("api/delta-reports")
        assert response.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def delta_report_list_view_without_filters(self):
        response = self.client.get("api/delta-reports")
        assert response.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)