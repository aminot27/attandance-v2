from django.db import models
from master_serv.models.base_model import BaseModel, status_types


class AttendanceRecord(BaseModel):
    attendance_id = models.AutoField(verbose_name='ID', primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name='Student')
    date = models.DateField(verbose_name='Date')
    status = models.CharField(verbose_name='Status', max_length=20, choices=status_types)

    class Meta:
        db_table = 'academy_attendance_record'
        ordering = ['attendance_id']
        verbose_name = 'Attendance Record'
        verbose_name_plural = 'Attendance Records'

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"