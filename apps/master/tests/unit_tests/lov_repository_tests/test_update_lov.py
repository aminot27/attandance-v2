from django.core.exceptions import FieldDoesNotExist
from django.db import DataError

from apps.master.models.lov_model import Lov
from apps.master.repositories.lov_repository import LovRepository
from apps.master.tests.unit_tests.test_base import BaseTestCase


class UpdateLovTestCases(BaseTestCase):
    """
    Successfully test cases
    """

    def test_update_lov(self):
        lov_id = 2
        update = {
            'code': 'u_code',
            'type': 'u_type'
        }
        updated_lov = LovRepository().update_lov(lov_id=lov_id, lov=update)
        self.assertIsInstance(updated_lov, Lov)
        self.assertEqual(updated_lov.lov_id, lov_id)
        self.assertEqual(updated_lov.code, 'u_code')
        self.assertEqual(updated_lov.type, 'u_type')

    """
    Unsuccessfully test cases
    """

    def test_update_lov_with_non_existing_id(self):
        lov_id = 99999
        update = {
            'code': 'u_code',
            'type': 'u_type'
        }
        updated_lov = LovRepository().update_lov(lov_id=lov_id, lov=update)
        self.assertIsNone(updated_lov)

    def test_update_lov_with_field_too_long(self):
        lov_id = 2
        update = {
            'code': 'updated_code',
            'type': 'updated_type'
        }
        updated_lov = LovRepository().update_lov(lov_id=lov_id, lov=update)
        self.assertIsInstance(updated_lov, DataError)

    def test_update_lov_with_invalid_fields(self):
        lov_id = 2
        update = {
            'invalid_type': 'type',
            'invalid_type_description': 'description'
        }
        updated_lov = LovRepository().update_lov(lov_id=lov_id, lov=update)
        self.assertIsInstance(updated_lov, FieldDoesNotExist)
