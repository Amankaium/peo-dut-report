from rest_framework.test import APITestCase
from core.models import *
from .factories import ReportFactory


class ReportAPITestCase(APITestCase):
    def setUp(self):
        report_object_1 = ReportFactory()
        report_object_2 = ReportFactory()

    def test_get_report_should_success(self):
        response = self.client.get("/api/reports/")
        assert response.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_get_one_report_should_return_200(self):
        response = self.client.get("/api/reports/1/")
        data = response.json()
        report_object = Report.objects.get(id=1)
        self.assertEqual(data["start_date"][0:10], str(report_object.start_date.date()))
        self.assertEqual(data["end_date"][0:10], str(report_object.end_date.date()))




