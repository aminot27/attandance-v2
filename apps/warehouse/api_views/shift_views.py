from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException, NotFound, ValidationError

# Asegúrate de importar correctamente los modelos, repositorios y serializadores de Shift
from apps.warehouse.models.shift_model import Shift
from apps.warehouse.repositories.shift_repository import ShiftRepository
from apps.warehouse.serializers.shift_serializers import (
    ShiftSerializer,
    ShiftDynamicResponse,
    ShiftCreateRequest,
    ShiftUpdateRequest
)
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView

class ShiftsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    shift_repository = ShiftRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: ShiftSerializer(many=True)})
    def get(self, request):
        try:
            shifts = self.shift_repository.get_shifts()
            return SuccessResponse(data_=ShiftSerializer(shifts, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: ShiftDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        shifts = self.shift_repository.post_shifts(*values, **params)
        if type(shifts) is FieldError:
            raise ValidationError(shifts)
        else:
            return SuccessResponse(
                data_=ShiftDynamicResponse(shifts, many=True, fields=values).data).send()

class ShiftView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    shift_repository = ShiftRepository()

    @swagger_auto_schema(request_body=ShiftCreateRequest, responses={status.HTTP_200_OK: ShiftSerializer()})
    def post(self, request):
        create_data = super().get_request_data(ShiftCreateRequest(data=request.data))
        try:
            shift = self.shift_repository.create_shift(create_data)
            return SuccessResponse(data_=ShiftSerializer(shift).data).send()
        except Exception as e:
            raise APIException(detail=f"Error creating shift: {e}")

class ShiftDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    shift_repository = ShiftRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: ShiftSerializer()})
    def get(self, request, pk):
        shift = self.shift_repository.get_shift(shift_id=pk)
        if shift is None:
            raise NotFound(detail="Shift not found")
        else:
            return SuccessResponse(data_=ShiftSerializer(shift).data).send()

    @swagger_auto_schema(request_body=ShiftUpdateRequest, responses={status.HTTP_200_OK: ShiftSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=ShiftUpdateRequest(data=request.data))
            shift = self.shift_repository.update_shift(shift_id=pk, shift=update_data)
            if shift is None:
                raise NotFound(detail="Shift not found")
            else:
                return SuccessResponse(data_=ShiftSerializer(shift).data).send()
        except:
            raise APIException()


    def delete(self, request, pk):
        shift = self.shift_repository.get_shift(shift_id=pk)
        deleted = self.shift_repository.soft_delete_shift(shift_id=pk)
        if deleted is None:
            raise NotFound(detail="Shift not found")
        else:
            return SuccessResponse(data_=ShiftSerializer(shift).data).send()