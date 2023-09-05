from rest_framework.test import APITestCase
from core.models import OperationType


class OperationTypeAPITestCase(APITestCase):
    def setUp(self):
        OperationType.objects.create(
            id_realcom=1,
            name='test name 1',
        )

        OperationType.objects.create(
            id_realcom=2,
            name='test name 2',
        )

    def get_operation_types_list_should_success(self):
        response = self.client.get('operation-types/')
        assert response.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_get_one_operation_types_should_return_200(self):
        response = self.client.get('/operation-types/1/')
        data = response.json()
        operation_object = OperationType.objects.get(id=1)
        self.assertEqual(data['id_realcom'], operation_object.id_realcom)
        self.assertEqual(data['name'], operation_object.name)
