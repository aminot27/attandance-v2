from django.contrib.auth.models import User
from django.db import models

from master_serv.models.base_model import BaseModel


class SystemUser(BaseModel):
    """docstring for SystemUser"""
    system_user_id = models.AutoField("System User Id", primary_key=True)
    auth_user = models.OneToOneField(User, on_delete=models.DO_NOTHING, db_column='auth_user_id', blank=False,
                                     null=False)
    document_type = models.CharField(max_length=10, blank=True, null=True, default='DNI')
    document = models.CharField(max_length=8, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=9, blank=True, null=True)
    entity = models.CharField(max_length=200, blank=True, null=True)
    avatar = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'master_system_user'
        ordering = ["system_user_id"]
        verbose_name_plural = "System Users"
        verbose_name = "System User"

    def __str__(self):
        return '{}'.format(self.auth_user.username)
