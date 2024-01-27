from rest_framework import serializers
from apps.warehouse.models.shift_model import Shift
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'

class ShiftDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = Shift
        exclude = ('status', 'modified')

class ShiftDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = Shift
        fields = ('start_time', 'end_time')

class ShiftBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ('start_time', 'end_time')

class ShiftCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Shift
        exclude = ('status', 'modified')

class ShiftUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Shift
        exclude = ('shift_id', 'status', 'modified')