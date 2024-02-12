from rest_framework import serializers
from apps.warehouse.models.shift_model import Shift
from apps.warehouse.models.weekly_shift_model import WeeklyShift  # Asegúrate de importar correctamente el modelo WeeklyShift
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class WeeklyShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyShift
        fields = '__all__'

class WeeklyShiftDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = WeeklyShift
        exclude = ('status', 'modified')

class WeeklyShiftDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = WeeklyShift
        fields = '__all__'  # Ajusta según necesidad, incluyendo todos los campos para solicitudes dinámicas

class WeeklyShiftBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyShift
        fields = ('monday_shift', 'tuesday_shift', 'wednesday_shift', 'thursday_shift', 'friday_shift', 'saturday_shift', 'sunday_shift')

class WeeklyShiftCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = WeeklyShift
        exclude = ('status', 'modified')

class WeeklyShiftUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = WeeklyShift
        exclude = ('weekly_shift_id', 'status', 'modified')