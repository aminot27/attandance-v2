from apps.master.models.lov_model import Lov

# Create your tests here.
from apps.master.repositories.lov_repository import LovRepository
from apps.master.tests.unit_tests.test_base import BaseTestCase


class GetLovTestCases(BaseTestCase):
    """
    Successfully test cases
    """

    def test_get_lov_with_existing_lov_id(self):
        lov_id = 1
        lov = LovRepository().get_lov(lov_id=lov_id)
        self.assertIsInstance(lov, Lov)
        self.assertEqual(lov.lov_id, lov_id)

    def test_get_lov_string_method(self):
        lov_id = 1
        lov = LovRepository().get_lov(lov_id=lov_id)
        expected_string = 'type - code'
        self.assertIsInstance(lov, Lov)
        self.assertEqual(str(lov), expected_string)

    def test_get_lov_with_non_existing_lov_id(self):
        lov_id = 9999
        self.assertIsNone(LovRepository().get_lov(lov_id=lov_id))

    """
    Unsuccessfully test cases
    """

    def test_get_lov_with_string_lov_id(self):
        with self.assertRaises(ValueError):
            LovRepository().get_lov(lov_id='string_id')

    def test_get_lov_with_None_lov_id(self):
        self.assertIsNone(LovRepository().get_lov(lov_id=None))

    def test_get_lov_with_special_char(self):
        with self.assertRaises(ValueError):
            LovRepository().get_lov(lov_id=int('$"#%$#%'))
