from django.db import models
from django.utils.timezone import now
from apps.warehouse.models.shift_model import Shift
from apps.warehouse.models.student_model import Student
from master_serv.models.base_model import BaseModel
from django.utils.timezone import localtime

# Asumiendo que estos son los tipos de estado definidos previamente
status_types = [('Early', 'Temprano'), ('Late', 'Tarde'), ('Absent', 'Ausente')]

class AttendanceRecord(BaseModel):
    attendance_id = models.AutoField(verbose_name='ID', primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, db_column='student_id', verbose_name='Estudiante', null=False)
    entry_time = models.DateTimeField(verbose_name='Hora de Entrada', auto_now_add=True)
    exit_time = models.DateTimeField(verbose_name='Hora de Salida', null=True, blank=True)
    status = models.CharField(max_length=12, choices=status_types, default='Absent', verbose_name='Estado de Asistencia')
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, verbose_name='Turno')

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
        self.determine_status()
        super().save(*args, **kwargs)

    def determine_status(self):
        # Ajuste para manejar DateTimeField
        if self.entry_time and self.shift:
            print(f"Entry Time: {self.entry_time}")
            print(f"Shift Start Time: {self.shift.start_time}")
            print(f"Shift End Time: {self.shift.end_time}")
            print(f"Early Start: {self.shift.early_start}")
            print(f"Early End: {self.shift.early_end}")
            print(f"Late Start: {self.shift.late_start}")
            print(f"Late End: {self.shift.late_end}")

            local_entry_time = localtime(self.entry_time)
            entry_time_hour = local_entry_time.time()

            # Ahora utiliza entry_time_hour para las comparaciones
            if self.shift.early_start and self.shift.early_end and self.shift.early_start <= entry_time_hour <= self.shift.early_end:
                self.status = 'Early'
            elif self.shift.late_start and self.shift.late_end and self.shift.late_start <= entry_time_hour <= self.shift.late_end:
                self.status = 'Late'
            elif self.shift.start_time <= entry_time_hour <= self.shift.end_time:
                self.status = 'Absent'
            else:
                self.status = 'Absent'