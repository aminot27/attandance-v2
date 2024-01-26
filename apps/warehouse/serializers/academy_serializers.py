from rest_framework import serializers
from apps.warehouse.models.academy_model import Academy
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer


class AcademySerializer(serializers.ModelSerializer):
    class Meta:
        model = Academy
        fields = '__all__'


class AcademyDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = Academy
        exclude = ('status', 'modified')


class AcademyDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = Academy
        fields = ('name', 'location')


class AcademyBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academy
        fields = ('name', 'location')


class AcademyCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Academy
        exclude = ('status', 'modified')


class AcademyUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Academy
        exclude = ('academy_id', 'status', 'modified')
