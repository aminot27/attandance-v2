from django.db import models
from master_serv.models.base_model import BaseModel

class Academy(BaseModel):
    academy_id = models.AutoField(verbose_name='ID', primary_key=True)
    name = models.CharField(verbose_name='Name', max_length=255)
    name2 = models.CharField(verbose_name='Name', max_length=255)
    location = models.CharField(verbose_name='Location', max_length=255)

    class Meta:
        db_table = 'academy_academy'
        ordering = ['academy_id']
        verbose_name = 'Academy'
        verbose_name_plural = 'Academies'

    def __str__(self):
        return self.name