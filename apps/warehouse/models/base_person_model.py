from django.db import models
from master_serv.models.base_model import BaseModel

class BasePerson(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Name')
    last_name = models.CharField(max_length=255, verbose_name='Last Name')
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], verbose_name='Gender')
    dni = models.CharField(max_length=8, verbose_name='DNI')
    phone_number = models.CharField(max_length=20, verbose_name='Phone Number')

    class Meta(BaseModel.Meta):
        abstract = True

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.dni}"