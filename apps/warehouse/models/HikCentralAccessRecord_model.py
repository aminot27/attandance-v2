from django.db import models
from master_serv.models.base_model import BaseModel

class HikCentralAccessRecord(BaseModel):
    employee_id = models.CharField(max_length=255, verbose_name="Employee ID")
    access_date_time = models.DateTimeField(verbose_name="Access Date and Time")
    access_date = models.DateField(verbose_name="Access Date")
    access_time = models.TimeField(verbose_name="Access Time")

    class Meta:
        verbose_name = "HikCentral Access Record"
        verbose_name_plural = "HikCentral Access Records"
        db_table = 'hikcentral_access_record'

    def __str__(self):
        return f"{self.employee_id} - {self.access_date_time}"