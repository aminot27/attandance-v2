from django.db import models

from apps.master.models.system_model import System
from master_serv.models.base_model import BaseModel


class Module(BaseModel):
    module_id = models.AutoField(primary_key=True)
    system = models.ForeignKey(System, models.DO_NOTHING, db_column='system_id', blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    version = models.CharField(max_length=10, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(blank=False, null=False)
    icon = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'master_module'
        ordering = ['module_id']
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):
        return '{}'.format(self.name)
