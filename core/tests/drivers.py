from rest_framework.test import APITestCase
from core.models import *
from .factories import DriversNameFactory
import factory


class DriverAPITestCase(APITestCase):
    def setUp(self):
        DriversName_object_1 = DriversNameFactory()
        DriversName_object_2 = DriversNameFactory()


    def test_get_fullname_should_success(self):
        response = self.client.get("/api/driversname/")
        assert response.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_get_one_fullname_should_return_200(self):
        response = self.client.get("/api/driversname/1/")
        data = response.json()
        fullname_object = DriversName.objects.get(id=1)
        self.assertEqual(data["full_name"], fullname_object.full_name)
