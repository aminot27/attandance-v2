from django.db import models
from master_serv.models.base_model import BaseModel


class Shift(BaseModel):
    shift_id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    early_start = models.TimeField(verbose_name='Inicio Temprano', null=True, blank=True)
    early_end = models.TimeField(verbose_name='Fin Temprano', null=True, blank=True)

    late_start = models.TimeField(verbose_name='Inicio Tarde', null=True, blank=True)
    late_end = models.TimeField(verbose_name='Fin Tarde', null=True, blank=True)

    leave_start = models.TimeField(verbose_name='Inicio Salida', null=True, blank=True)
    leave_end = models.TimeField(verbose_name='Fin Salida', null=True, blank=True)

    def __str__(self):
        return self.name