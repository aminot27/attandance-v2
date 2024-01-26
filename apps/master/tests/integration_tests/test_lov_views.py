import datetime

from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse, path, include, get_resolver
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.test import APITestCase, APIClient, URLPatternsTestCase

from apps.master.models.lov_model import Lov


def get_fake_token():
    login = {
        'username': "test",
        'password': 'myTestPassword@2023'
    }
    tob = TokenObtainPairSerializer()
    tob.validate(login)
    refresh = tob.get_token(tob.user)
    return str(refresh.access_token)


class LovViewsTestCases(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/master/', include('apps.master.urls')),
    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(email='test@email.com', username='test', first_name='test',
                                 last_name='test', password='myTestPassword@2023')
        Lov.objects.create(lov_id=1, type='type', type_description='type description', code='code',
                           code_description='code description')
        Lov.objects.create(lov_id=2, type='type2', type_description='type description2', code='code2',
                           code_description='code description2')

    def test_get_lovs_without_params(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + get_fake_token())
        url = reverse('filter_lovs')
        response = self.client.get(url)
        result = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(result['data']), 2)
        self.assertEqual(result['status'], True)
        self.assertEqual(result['message'], "Process executed successfully")

    def test_get_lovs_with_params(self):
        fields = ['type', 'code']
        params = {
            'type': 'type'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + get_fake_token())
        url = reverse('filter_lovs')
        response = self.client.post(url, {'params': params, 'values': fields})
        result = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(result['data']), 1)
        self.assertEqual(result['status'], True)
        self.assertEqual(result['message'], "Process executed successfully")
        self.assertEqual(result['data'][0]['type'], 'type')

    def test_get_lovs_with_wrong_fields(self):
        fields = ['wrong_type', 'wrong_code']
        params = {
            'type': 'type'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + get_fake_token())
        url = reverse('filter_lovs')
        response = self.client.post(url, {'params': params, 'values': fields})
        result = response.data
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(result['status'], False)
        self.assertEqual(result['message'], "BAD REQUEST")
        self.assertEqual(result['data'], None)

    def test_create_lov_with_existing_lo_id(self):
        lov = {
            'lov_id': 1,
            'type': 'type3',
            'type_description': 'type_description3',
            'code': 'code3',
            'code_description': 'code description3'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + get_fake_token())
        url = reverse('create_lov')
        response = self.client.post(url, lov)
        result = response.data
        self.assertEqual(status.HTTP_500_INTERNAL_SERVER_ERROR, response.status_code)
        self.assertEqual(result['data'], None)
        self.assertEqual(result['status'], False)
        self.assertEqual(result['message'], "INTERNAL SERVER ERROR")

    def test_update_lov(self):
        lov_id = 1
        update = {
            'code': 'u_code',
            'code_description': 'u_code',
            'type': 'u_type',
            'type_description': 'u_type'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + get_fake_token())
        url = reverse('lov_detail', kwargs={'pk': lov_id})
        response = self.client.put(url, update)
        result = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(result['status'], True)
        self.assertEqual(result['message'], "Process executed successfully")
        self.assertEqual(result['data']['lov_id'], 1)

    def test_delete_lov(self):
        lov_id = 2
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + get_fake_token())
        url = reverse('lov_detail', kwargs={'pk': lov_id})
        response = self.client.delete(url)
        result = response.data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(result['status'], True)
        self.assertEqual(result['message'], "Process executed successfully")
