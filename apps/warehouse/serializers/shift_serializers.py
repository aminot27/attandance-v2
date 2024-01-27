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
    # Asegúrate de incluir los nuevos campos en las solicitudes dinámicas si es necesario
    class Meta:
        model = Shift
        fields = '__all__'  # Actualizado para incluir todos los campos, ajusta según necesidad

class ShiftBasicSerializer(serializers.ModelSerializer):
    # Actualiza este serializador si necesitas incluir los nuevos campos en una versión "básica"
    class Meta:
        model = Shift
        fields = ('start_time', 'end_time', 'early_tolerance_until', 'late_tolerance_until')  # Campos actualizados

class ShiftCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Shift
        exclude = ('status', 'modified')
        # No se necesita cambiar este si ya excluye 'status' y 'modified', y quieres incluir todos los demás campos

class ShiftUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Shift
        exclude = ('shift_id', 'status', 'modified')
        # Similar al ShiftCreateRequest, no necesita cambios si la intención es excluir solo estos campos