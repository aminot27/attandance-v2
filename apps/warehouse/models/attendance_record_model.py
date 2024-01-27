from django.db import models

from apps.warehouse.models.shift_model import Shift
from apps.warehouse.models.student_model import Student
from master_serv.models.base_model import BaseModel, status_types


class AttendanceRecord(BaseModel):
    attendance_id = models.AutoField(verbose_name='ID', primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, db_column='student_id', verbose_name='Student', null=False)
    entry_time = models.DateTimeField(auto_now_add=True, verbose_name='Entry Time')
    status = models.CharField(max_length=10, choices=status_types, default='Present', verbose_name='Attendance Status')
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, verbose_name='Shift')

    class Meta:
        db_table = 'academy_attendance_record'
        ordering = ['attendance_id']
        verbose_name = 'Attendance Record'
        verbose_name_plural = 'Attendance Records'

    def __str__(self):
        return f"{self.student} - {self.entry_time}"