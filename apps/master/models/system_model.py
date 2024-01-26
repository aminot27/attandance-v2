"""
SYSTEM INFORMATION MODELS
"""
from django.db import models

from master_serv.models.base_model import BaseModel


class System(BaseModel):
    system_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    icon = models.CharField(max_length=30, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    version = models.CharField(max_length=5, blank=True, null=True)
    order = models.IntegerField(blank=False, null=False)
    url = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        db_table = 'master_system'
        ordering = ['system_id']
        verbose_name = 'System'
        verbose_name_plural = 'Systems'

    def __str__(self):
        return '{}'.format(self.name)
