from django.db import models

from apps.master.models.profile_model import Profile
from apps.master.models.system_user_model import SystemUser
from master_serv.models.base_model import BaseModel


class SystemUserProfile(BaseModel):
    system_user_profile_id = models.AutoField(primary_key=True)
    system_user = models.ForeignKey(SystemUser, models.DO_NOTHING, db_column='system_user_id', blank=False, null=False)
    profile = models.ForeignKey(Profile, models.DO_NOTHING, db_column='profile_id', blank=False, null=False)

    class Meta:
        db_table = 'master_system_user_profile'
        ordering = ['system_user_profile_id']
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return '{}'.format(self.system_user.auth_user.first_name + ' - ' + self.profile.description)
