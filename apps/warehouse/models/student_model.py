from django.db import models

from apps.warehouse.models.base_person_model import BasePerson
from apps.warehouse.models.parent_model import Parent

from master_serv.models.base_model import BaseModel

class Student(BasePerson):
    student_id = models.AutoField(primary_key=True, verbose_name='ID')
    parent = models.ForeignKey(Parent, on_delete=models.DO_NOTHING, db_column='parent_id',
                               verbose_name='Parent', null=False)

    class Meta(BasePerson.Meta):
        verbose_name = 'Student'
        verbose_name_plural = 'Students'