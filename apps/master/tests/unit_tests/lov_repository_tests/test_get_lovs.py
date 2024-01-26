from django.core.exceptions import FieldError
from django.db.models import QuerySet

from apps.master.models.lov_model import Lov
from apps.master.repositories.lov_repository import LovRepository
from apps.master.tests.unit_tests.test_base import BaseTestCase


class GetLovsTestCases(BaseTestCase):
    """
    Successfully test cases
    """

    def test_get_lovs_without_params(self):
        lovs = LovRepository().get_lovs()
        self.assertIsInstance(lovs, QuerySet)
        self.assertEqual(len(lovs), 2)

    def test_get_lovs_with_params(self):
        values = ['type', 'code']
        params = {
            'type': 'type'
        }
        lovs = LovRepository().get_lovs(*values, **params)
        self.assertIsInstance(lovs, QuerySet)
        self.assertEqual(len(lovs), 1)
        self.assertEqual(lovs[0]['type'], 'type')
        self.assertQuerysetEqual(lovs, [{'type': 'type', 'code': 'code'}])

    def test_get_lovs_with_non_existing_params(self):
        fields = ['type', 'code']
        params = {
            'type': 'non_existing_type'
        }
        lovs = LovRepository().get_lovs(*fields, **params)
        self.assertIsInstance(lovs, QuerySet)
        self.assertEqual(len(lovs), 0)

    """
    Unsuccessfully test cases
    """

    def test_get_lovs_with_wrong_fields(self):
        fields = ['wrong_type', 'wrong_code']
        params = {
            'type': 'type'
        }
        lovs = LovRepository().get_lovs(*fields, **params)
        self.assertIsInstance(lovs, FieldError)

    def test_get_lovs_with_wrong_params(self):
        fields = ['type', 'code']
        params = {
            'wrong_type': 'type'
        }
        lovs = LovRepository().get_lovs(*fields, **params)
        self.assertIsInstance(lovs, FieldError)
