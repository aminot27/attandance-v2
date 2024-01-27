from django.contrib import admin
from apps.warehouse.models.academy_model import Academy
from apps.warehouse.models.attendance_record_model import AttendanceRecord
from apps.warehouse.models.location_record_model import LocationRecord
from apps.warehouse.models.parent_model import Parent
from apps.warehouse.models.shift_model import Shift
from apps.warehouse.models.student_model import Student


@admin.register(Academy)
class AcademyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Academy._meta.fields]


@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AttendanceRecord._meta.fields]


@admin.register(LocationRecord)
class LocationRecordAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LocationRecord._meta.fields]


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Parent._meta.fields]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Shift._meta.fields]
