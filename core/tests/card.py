from rest_framework.test import APITestCase
from core.models import Card


class CardAPITestCase(APITestCase):
    def setUp(self):
        Card.objects.create(
            id_realcom='11',
            number='11'
        )

        Card.objects.create(
            id_realcom='22',
            number='22'
        )

    def test_get_card_list_should_success(self):
        response = self.client.get("/cards/")
        assert response.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)


    def test_get_one_card_should_return_200(self):
        response = self.client.get("/cards/1/")
        data = response.json()
        card_object = Card.objects.get(id=1)
        self.assertEqual(data["id_realcom"], card_object.id_realcom)
        self.assertEqual(data["number"], card_object.number)