from rest_framework import serializers
from apps.warehouse.models.attendance_record_model import AttendanceRecord
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = '__all__'

class AttendanceRecordDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = AttendanceRecord
        exclude = ('status', 'modified')

class AttendanceRecordDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = ('student', 'date', 'status')

class AttendanceRecordBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = ('student', 'date', 'status')

class AttendanceRecordCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        exclude = ('status', 'modified')

class AttendanceRecordUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        exclude = ('attendance_id', 'status', 'modified')