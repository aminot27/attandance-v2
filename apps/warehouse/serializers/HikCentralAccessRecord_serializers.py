from rest_framework import serializers
from apps.warehouse.models.HikCentralAccessRecord_model import HikCentralAccessRecord
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class HikCentralAccessRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HikCentralAccessRecord
        fields = '__all__'

class HikCentralAccessRecordDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = HikCentralAccessRecord
        exclude = ('status', 'modified')

class HikCentralAccessRecordDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = HikCentralAccessRecord
        fields = '__all__'

class HikCentralAccessRecordBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = HikCentralAccessRecord
        fields = ('employee_id', 'access_date_time', 'access_date', 'access_time')

class HikCentralAccessRecordCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = HikCentralAccessRecord
        exclude = ('status', 'modified')

class HikCentralAccessRecordUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = HikCentralAccessRecord
        exclude = ('employee_id', 'status', 'modified')