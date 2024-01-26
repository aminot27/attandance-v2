from rest_framework import serializers

from apps.master.models.lov_model import Lov
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer


class LovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lov
        fields = '__all__'


class LovDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = Lov
        exclude = ('status', 'modified')


class LovdDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = Lov
        fields = ('type', 'type_description', 'code', 'code_description')


class LovBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lov
        fields = ('type', 'type_description', 'code', 'code_description')


class LovCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Lov
        exclude = ('status', 'modified')


class LovUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Lov
        exclude = ("lov_id", "status", "modified")
