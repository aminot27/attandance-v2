from django.db import models
from master_serv.models.base_model import BaseModel

class LocationRecord(BaseModel):
    location_id = models.AutoField(verbose_name='ID', primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name='Student')
    timestamp = models.DateTimeField(verbose_name='Timestamp')
    latitude = models.DecimalField(verbose_name='Latitude', max_digits=9, decimal_places=6)
    longitude = models.DecimalField(verbose_name='Longitude', max_digits=9, decimal_places=6)

    class Meta:
        db_table = 'academy_location_record'
        ordering = ['location_id']
        verbose_name = 'Location Record'
        verbose_name_plural = 'Location Records'

    def __str__(self):
        return f"{self.student} - {self.timestamp}"