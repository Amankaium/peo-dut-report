from rest_framework.test import APITestCase
from core.models import *
from .factories import StationFactory
import factory


class StationAPITestCase(APITestCase):
    def setUp(self):
        station_object_1 = StationFactory()
        station_object_2 = StationFactory()


    def test_get_station_should_success(self):
        response = self.client.get("/api/stations/")
        assert response.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_get_one_station_should_return_200(self):
        response = self.client.get("/api/stations/1/")
        data = response.json()
        station_object = Station.objects.get(id=1)
        self.assertEqual(data["name"], station_object.name)
