from rest_framework import serializers
from apps.warehouse.models.location_record_model import LocationRecord
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class LocationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationRecord
        fields = '__all__'

class LocationRecordDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = LocationRecord
        exclude = ('status', 'modified')

class LocationRecordDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = LocationRecord
        fields = ('student', 'timestamp', 'latitude', 'longitude')

class LocationRecordBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationRecord
        fields = ('student', 'timestamp', 'latitude', 'longitude')

class LocationRecordCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = LocationRecord
        exclude = ('status', 'modified')

class LocationRecordUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = LocationRecord
        exclude = ('location_id', 'status', 'modified')