from django.core.exceptions import ObjectDoesNotExist

from apps.master.models.lov_model import Lov
from apps.master.repositories.lov_repository import LovRepository
from apps.master.tests.unit_tests.test_base import BaseTestCase


class DeleteLovTestCases(BaseTestCase):
    def test_delete_lov(self):
        lov_id = 2
        result = LovRepository().delete_lov(lov_id=lov_id)
        self.assertTrue(result)
        with self.assertRaises(ObjectDoesNotExist):
            Lov.objects.get(lov_id=lov_id)

    def test_delete_lov_with_non_exist_lov_id(self):
        lov_id = 9999
        result = LovRepository().delete_lov(lov_id=lov_id)
        self.assertIsNone(result)
