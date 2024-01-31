from rest_framework import serializers
from apps.warehouse.models.student_model import Student
from apps.warehouse.models.attendance_record_model import AttendanceRecord

class ScanDniRequestSerializer(serializers.Serializer):
    dni = serializers.CharField(max_length=100)

class AttendanceRecordDniSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = '__all__'