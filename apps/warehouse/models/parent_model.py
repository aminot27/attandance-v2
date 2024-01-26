from django.contrib.auth.models import User
from django.db import models

from apps.warehouse.models.base_person_model import BasePerson
from master_serv.models.base_model import BaseModel

class Parent(BasePerson):
    parent_id = models.AutoField(primary_key=True, verbose_name='ID')

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.dni}"

    class Meta(BasePerson.Meta):
        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'