from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException, NotFound, ValidationError

from apps.warehouse.models.attendance_record_model import AttendanceRecord
from apps.warehouse.repositories.attendance_record_repository import AttendanceRecordRepository
from apps.warehouse.serializers.attendance_record_serializers import (
    AttendanceRecordSerializer,
    AttendanceRecordDynamicResponse,
    AttendanceRecordCreateRequest,
    AttendanceRecordUpdateRequest
)
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView

class AttendanceRecordsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    attendance_record_repository = AttendanceRecordRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: AttendanceRecordSerializer(many=True)})
    def get(self, request):
        try:
            attendance_records = self.attendance_record_repository.get_attendance_records()
            return SuccessResponse(data_=AttendanceRecordSerializer(attendance_records, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: AttendanceRecordDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        attendance_records = self.attendance_record_repository.post_attendance_records(*values, **params)
        if type(attendance_records) is FieldError:
            raise ValidationError(attendance_records)
        else:
            return SuccessResponse(
                data_=AttendanceRecordDynamicResponse(attendance_records, many=True, fields=values).data).send()

class AttendanceRecordView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    attendance_record_repository = AttendanceRecordRepository()

    @swagger_auto_schema(request_body=AttendanceRecordCreateRequest, responses={status.HTTP_200_OK: AttendanceRecordSerializer()})
    def post(self, request):
        create_data = super().get_request_data(AttendanceRecordCreateRequest(data=request.data))
        try:
            attendance_record = self.attendance_record_repository.create_attendance_record(create_data)
            return SuccessResponse(data_=AttendanceRecordSerializer(attendance_record).data).send()
        except:
            raise APIException(detail="Error creating attendance record")

class AttendanceRecordDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    attendance_record_repository = AttendanceRecordRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: AttendanceRecordSerializer()})
    def get(self, request, pk):
        attendance_record = self.attendance_record_repository.get_attendance_record(attendance_id=pk)
        if attendance_record is None:
            raise NotFound(detail="Attendance record not found")
        else:
            return SuccessResponse(data_=AttendanceRecordSerializer(attendance_record).data).send()

    @swagger_auto_schema(request_body=AttendanceRecordUpdateRequest, responses={status.HTTP_200_OK: AttendanceRecordSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=AttendanceRecordUpdateRequest(data=request.data))
            attendance_record = self.attendance_record_repository.update_attendance_record(attendance_id=pk, attendance_record=update_data)
            if attendance_record is None:
                raise NotFound(detail="Attendance record not found")
            else:
                return SuccessResponse(data_=AttendanceRecordSerializer(attendance_record).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        attendance_record = self.attendance_record_repository.get_attendance_record(attendance_id=pk)
        deleted = self.attendance_record_repository.soft_delete_attendance_record(attendance_id=pk)
        if deleted is None:
            raise NotFound(detail="Attendance record not found")
        else:
            return SuccessResponse(data_=AttendanceRecordSerializer(attendance_record).data).send()