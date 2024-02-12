import traceback

from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException, NotFound, ValidationError

# Asegúrate de importar correctamente el modelo WeeklyShift y los serializadores necesarios
from apps.warehouse.models.weekly_shift_model import WeeklyShift
from apps.warehouse.repositories.weekly_shift_repository import WeeklyShiftRepository
from apps.warehouse.serializers.weekly_shift_serializers import (
    WeeklyShiftSerializer,
    WeeklyShiftDynamicResponse,
    WeeklyShiftCreateRequest,
    WeeklyShiftUpdateRequest
)
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView

class WeeklyShiftsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    weekly_shift_repository = WeeklyShiftRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: WeeklyShiftSerializer(many=True)})
    def get(self, request):
        try:
            weekly_shifts = self.weekly_shift_repository.get_weekly_shifts()
            return SuccessResponse(data_=WeeklyShiftSerializer(weekly_shifts, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: WeeklyShiftDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        weekly_shifts = self.weekly_shift_repository.post_weekly_shifts(*values, **params)
        if type(weekly_shifts) is FieldError:
            raise ValidationError(weekly_shifts)
        else:
            return SuccessResponse(
                data_=WeeklyShiftDynamicResponse(weekly_shifts, many=True, fields=values).data).send()

class WeeklyShiftView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    weekly_shift_repository = WeeklyShiftRepository()

    @swagger_auto_schema(request_body=WeeklyShiftCreateRequest, responses={status.HTTP_200_OK: WeeklyShiftSerializer()})
    def post(self, request):
        create_data = super().get_request_data(WeeklyShiftCreateRequest(data=request.data))
        monday = create_data.get('shift')
        tuesday = create_data.get('shift')
        wednesday = create_data.get('shift')
        thursday = create_data.get('shift')
        friday = create_data.get('shift')
        saturday = create_data.get('shift')
        sunday = create_data.get('shift')

        try:
            weekly_shift = self.weekly_shift_repository.create_weekly_shift(create_data)
            return SuccessResponse(data_=WeeklyShiftSerializer(weekly_shift).data).send()
        except Exception as e:
            raise APIException(detail=f"Error creating weekly shift: {e}")

class WeeklyShiftDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    weekly_shift_repository = WeeklyShiftRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: WeeklyShiftSerializer()})
    def get(self, request, pk):
        weekly_shift = self.weekly_shift_repository.get_weekly_shift(weekly_shift_id=pk)
        if weekly_shift is None:
            raise NotFound(detail="Weekly shift not found")
        else:
            return SuccessResponse(data_=WeeklyShiftSerializer(weekly_shift).data).send()

    @swagger_auto_schema(request_body=WeeklyShiftUpdateRequest, responses={status.HTTP_200_OK: WeeklyShiftSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=WeeklyShiftUpdateRequest(data=request.data))
            weekly_shift = self.weekly_shift_repository.update_weekly_shift(weekly_shift_id=pk, weekly_shift_data=update_data)
            if weekly_shift is None:
                raise NotFound(detail="Weekly shift not found")
            else:
                return SuccessResponse(data_=WeeklyShiftSerializer(weekly_shift).data).send()
        except:
            tb = traceback.format_exc()
            print(tb)
            raise APIException()

    def delete(self, request, pk):
        weekly_shift = self.weekly_shift_repository.get_weekly_shift(weekly_shift_id=pk)
        deleted = self.weekly_shift_repository.soft_delete_weekly_shift(weekly_shift_id=pk)
        if deleted is None:
            raise NotFound(detail="Weekly shift not found")
        else:
            return SuccessResponse(data_=WeeklyShiftSerializer(weekly_shift).data).send()