from rest_framework.test import APITestCase
from core.models import *


class StationAPITestCase(APITestCase):
    def setUp(self):
        Station.objects.create(name='Наименование', id_realcom=1)
        Station.objects.create(name='Наименование2', id_realcom=2)

    def test_get_station_list_should_success(self):
        response = self.client.get("/stations/")
        assert response.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_get_one_station_should_return_200(self):
        response = self.client.get("stations/1/")
        data = response.json()
        station_object = Station.objects.get(id=1)
        self.assertEqual(data["station"], station_object.station)
        self.assertEqual(data["id_realcom"], station_object.id_realcom)


class StationCreateAPITestCase(APITestCase):
    def setUp(self):
        self.url = '/stations-create/'

    def test_post_empty_data(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 400)

    def test_post_data_should_success(self):
        data = {"station": "Наименование", "id_realcom": 1}
        response = self.client.post(path=self.url, data=data)
        self.assertEqual(response.status_code, 201)
        new_station = Station.objects.get(station=data["station"])
        self.assertEqual(data["id_realcom"], new_station.id_realcom)
