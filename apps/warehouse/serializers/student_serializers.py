from rest_framework import serializers
from apps.warehouse.models.student_model import Student
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = Student
        exclude = ('status', 'modified')

class StudentDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = Student
        fields = ('user', 'registration_number')

class StudentBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user', 'registration_number')

class StudentCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ('status', 'modified')

class StudentUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ('student_id', 'status', 'modified')