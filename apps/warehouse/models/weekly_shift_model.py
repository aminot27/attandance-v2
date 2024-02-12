from django.db import models
from apps.warehouse.models.shift_model import Shift
from master_serv.models.base_model import BaseModel


class WeeklyShift(BaseModel):
    weekly_shift_id = models.AutoField(primary_key=True, verbose_name='Weekly shift')
    monday_shift = models.ForeignKey(Shift, on_delete=models.CASCADE, null=True, blank=True, related_name='monday_shifts')
    tuesday_shift = models.ForeignKey(Shift, on_delete=models.CASCADE, null=True, blank=True, related_name='tuesday_shifts')
    wednesday_shift = models.ForeignKey(Shift, on_delete=models.CASCADE, null=True, blank=True, related_name='wednesday_shifts')
    thursday_shift = models.ForeignKey(Shift, on_delete=models.CASCADE, null=True, blank=True, related_name='thursday_shifts')
    friday_shift = models.ForeignKey(Shift, on_delete=models.CASCADE, null=True, blank=True, related_name='friday_shifts')
    saturday_shift = models.ForeignKey(Shift, on_delete=models.CASCADE, null=True, blank=True, related_name='saturday_shifts')
    sunday_shift = models.ForeignKey(Shift, on_delete=models.CASCADE, null=True, blank=True, related_name='sunday_shifts')

    def __str__(self):
        return f"Weekly Shift Schedule ID: {self.id}"

    class Meta:
        verbose_name = 'Weekly Shift'
        verbose_name_plural = 'Weekly Shifts'
        db_table = 'weekly_shifts'