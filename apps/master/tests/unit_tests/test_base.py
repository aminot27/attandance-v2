from django.test import TestCase

from apps.master.models.lov_model import Lov


class BaseTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        __test__ = False
        Lov.objects.create(lov_id=1, type='type', type_description='type description', code='code',
                           code_description='code description')
        Lov.objects.create(lov_id=2, type='type2', type_description='type description2', code='code2',
                           code_description='code description2')
