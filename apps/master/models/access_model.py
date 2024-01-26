from django.db import models

from apps.master.models.module_model import Module
from apps.master.models.profile_model import Profile
from master_serv.models.base_model import BaseModel


class Access(BaseModel):
    access_id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, models.DO_NOTHING, db_column='profile_id', blank=False, null=False)
    module = models.ForeignKey(Module, models.DO_NOTHING, db_column='module_id', blank=False, null=False)

    class Meta:
        db_table = 'master_access'
        ordering = ['access_id']
        verbose_name = 'Access'
        verbose_name_plural = 'Access'

    def __str__(self):
        return '{}'.format(str(self.access_id))
