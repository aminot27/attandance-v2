from django.db import models
from master_serv.models.base_model import BaseModel

class Shift(BaseModel):
    shift_id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name