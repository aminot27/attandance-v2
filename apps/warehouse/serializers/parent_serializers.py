from rest_framework import serializers
from apps.warehouse.models.parent_model import Parent
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class ParentDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = Parent
        exclude = ('status', 'modified')

class ParentDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = Parent
        fields = ('user', 'phone', 'email')

class ParentBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('user', 'phone', 'email')

class ParentCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Parent
        exclude = ('status', 'modified')

class ParentUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Parent
        exclude = ('parent_id', 'status', 'modified')