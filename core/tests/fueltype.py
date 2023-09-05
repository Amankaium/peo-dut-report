from rest_framework.test import APITestCase
from core.models import *


class FuelTypeAPITestCase(APITestCase):
    def setUp(self):
        FuelType.objects.create(fuel='test 1', id_realcom=1)
        FuelType.objects.create(fuel='test 2', id_realcom=2)
    def test_get_fuel_list_should_success(self):
        response = self.client.get("/fuel-types/")
        assert response.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_get_one_fuel_should_return_200(self):
        response = self.client.get("/fuel-types-detail/1/")
        data = response.json()
        fuel_object = FuelType.objects.get(id=1)
        self.assertEqual(data["fuel"], fuel_object.fuel)
        self.assertEqual(data["id_realcom"], fuel_object.id_realcom)

class FuelTypeCreateAPITestCase(APITestCase):
    def setUp(self):
        self.url = '/fuel-types-create/'

    def test_get_request_to_create_api_should_return_405(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)

    def test_post_empty_data(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 400)

    def test_post_data_should_success(self):
        data = {"fuel": "test 1", "id_realcom": 1}
        response = self.client.post(path=self.url, data=data)
        self.assertEqual(response.status_code, 201)
        new_fuel = FuelType.objects.get(fuel=data["fuel"])
        self.assertEqual(data["id_realcom"], new_fuel.id_realcom)