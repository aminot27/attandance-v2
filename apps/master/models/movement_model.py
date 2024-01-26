from django.db import models

from apps.master.models.system_user_model import SystemUser
from master_serv.models.base_model import BaseModel


class Movement(BaseModel):
    movement_id = models.AutoField(primary_key=True)
    system_user = models.ForeignKey(SystemUser, models.DO_NOTHING, db_column='system_user_id', blank=False, null=False)
    movement_type = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=30, blank=True, null=True)
    table = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'master_movement'
        ordering = ['movement_id']
        verbose_name = 'Movement'
        verbose_name_plural = 'Movements'

    def __str__(self):
        return '{}'.format(self.movement_type + ' - ' + self.table)
