from rest_framework.test import APITestCase
from .factories import CardOperation


class CardOperationTestCase(APITestCase):
    def setUp(self):
        object_1 = CardOperation()
        object_2 = CardOperation()
        object_3 = CardOperation()
    
    def test_check_list_should_return_200(self):
        response = self.client.get("/api/card-operations/")
        self.assertEqual(response.status_code, 200)
        qty = len(response.json())
        self.assertEqual(qty, 3)