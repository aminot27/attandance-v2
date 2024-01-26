from django.db import models

from master_serv.models.base_model import BaseModel


class Profile(BaseModel):
    profile_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    domain = models.CharField(max_length=20, blank=False, null=False)
    type = models.CharField(max_length=15, blank=True, null=True)
    icon = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'master_profile'
        ordering = ['profile_id']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return '{}'.format(self.name)
