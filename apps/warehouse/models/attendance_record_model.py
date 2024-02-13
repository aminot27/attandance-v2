from django.db import models
from django.utils.timezone import now, localtime
from apps.warehouse.models.shift_model import Shift
from apps.warehouse.models.student_model import Student
from master_serv.models.base_model import BaseModel

# Asumiendo que estos son los tipos de estado definidos previamente
status_types = [('Early', 'Temprano'), ('Late', 'Tarde'), ('Absent', 'Ausente')]

class AttendanceRecord(BaseModel):
    attendance_id = models.AutoField(verbose_name='ID', primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, db_column='student_id', verbose_name='Estudiante', null=False)
    entry_time = models.DateTimeField(verbose_name='Hora de Entrada', auto_now_add=True)
    exit_time = models.DateTimeField(verbose_name='Hora de Salida', null=True, blank=True)
    status = models.CharField(max_length=12, choices=status_types, default='Absent', verbose_name='Estado de Asistencia')
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, verbose_name='Turno')
    entry_sms_sent = models.BooleanField(default=False)
    exit_sms_sent = models.BooleanField(default=False)
    class Meta:
        db_table = 'academy_attendance_record'
        ordering = ['attendance_id']
        verbose_name = 'Registro de Asistencia'
        verbose_name_plural = 'Registros de Asistencia'

    def __str__(self):
        return f"{self.student} - {self.entry_time}"

    def save(self, *args, **kwargs):
        if not self.entry_time:
            self.entry_time = now()
        super().save(*args, **kwargs)

