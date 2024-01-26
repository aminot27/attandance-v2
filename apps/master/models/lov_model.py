"""
LIST OF VALUES TABLE
"""
from django.db import models

from master_serv.models.base_model import BaseModel


class Lov(BaseModel):
    lov_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, blank=False)
    type_description = models.CharField(max_length=200, blank=False)
    code = models.CharField(max_length=20, blank=False)
    code_description = models.CharField(max_length=200, blank=False)

    class Meta:
        db_table = 'master_lov'
        ordering = ['lov_id']
        verbose_name = 'LOV'
        verbose_name_plural = 'LOVs'

    def __str__(self):
        return '{}'.format(str(self.type) + " - " + str(self.code))
