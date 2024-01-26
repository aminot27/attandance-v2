from django.db import IntegrityError, DataError

from apps.master.models.lov_model import Lov
from apps.master.repositories.lov_repository import LovRepository
from apps.master.tests.unit_tests.test_base import BaseTestCase


class CreateLovTestCases(BaseTestCase):
    """
    Successfully test cases
    """

    def test_create_lov(self):
        lov = {
            'lov_id': 3,
            'type': 'type3',
            'type_description': 'type_description3',
            'code': 'code3',
            'code_description': 'code description3'
        }
        created_lov = LovRepository().create_lov(lov)
        self.assertIsInstance(created_lov, Lov)
        self.assertEqual(created_lov.lov_id, 3)
        self.assertEqual(created_lov.status, 'CREATED')
        self.assertEqual(Lov.objects.count(), 3)

    def test_create_lov_with_blank_field(self):
        lov = {
            'lov_id': 3,
            'code': '',
        }
        created_lov = LovRepository().create_lov(lov)
        self.assertIsInstance(created_lov, Lov)
        self.assertEqual(created_lov.code, '')

    """
        Unsuccessfully test cases
    """

    def test_create_lov_with_existing_lov_id(self):
        lov = {
            'lov_id': 2,
            'type': 'type',
            'type_description': 'type_description',
            'code': 'code',
            'code_description': 'code description'
        }
        created_lov = LovRepository().create_lov(lov)
        self.assertIsInstance(created_lov, IntegrityError)

    def test_create_lov_with_field_too_long(self):
        lov = {
            'lov_id': 3,
            'code': 'codeeeeeeeeeeeeeeeeeeeeeeeeeeee',
        }
        created_lov = LovRepository().create_lov(lov)
        self.assertIsInstance(created_lov, DataError)

    def test_create_lov_with_invalid_fields(self):
        lov = {
            'lov_id': 3,
            'invalid_type': 'type',
            'invalid_type_description': 'description'
        }
        created_lov = LovRepository().create_lov(lov)
        self.assertIsInstance(created_lov, TypeError)
