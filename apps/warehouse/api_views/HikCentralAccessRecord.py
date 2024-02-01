from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException, NotFound, ValidationError

# Importa los modelos, repositorios y serializadores de HikCentralAccessRecord
from apps.warehouse.repositories.HikCentralAccessRecord_repository import HikCentralAccessRecordRepository
from apps.warehouse.serializers.HikCentralAccessRecord_serializers import (
    HikCentralAccessRecordSerializer,
    HikCentralAccessRecordDynamicResponse,
    HikCentralAccessRecordCreateRequest,
    HikCentralAccessRecordUpdateRequest
)
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView

class HikCentralAccessRecordsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    hikcentral_access_record_repository = HikCentralAccessRecordRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: HikCentralAccessRecordSerializer(many=True)})
    def get(self, request):
        try:
            records = self.hikcentral_access_record_repository.get_records()
            return SuccessResponse(data_=HikCentralAccessRecordSerializer(records, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: HikCentralAccessRecordDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        records = self.hikcentral_access_record_repository.post_records(*values, **params)
        if type(records) is FieldError:
            raise ValidationError(records)
        else:
            return SuccessResponse(
                data_=HikCentralAccessRecordDynamicResponse(records, many=True, fields=values).data).send()

class HikCentralAccessRecordView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    hikcentral_access_record_repository = HikCentralAccessRecordRepository()

    @swagger_auto_schema(request_body=HikCentralAccessRecordCreateRequest, responses={status.HTTP_200_OK: HikCentralAccessRecordSerializer()})
    def post(self, request):
        create_data = super().get_request_data(HikCentralAccessRecordCreateRequest(data=request.data))
        try:
            record = self.hikcentral_access_record_repository.create_record(create_data)
            return SuccessResponse(data_=HikCentralAccessRecordSerializer(record).data).send()
        except Exception as e:
            raise APIException(detail=f"Error creating record: {e}")

class HikCentralAccessRecordDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    hikcentral_access_record_repository = HikCentralAccessRecordRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: HikCentralAccessRecordSerializer()})
    def get(self, request, pk):
        record = self.hikcentral_access_record_repository.get_record(record_id=pk)
        if record is None:
            raise NotFound(detail="Record not found")
        else:
            return SuccessResponse(data_=HikCentralAccessRecordSerializer(record).data).send()

    @swagger_auto_schema(request_body=HikCentralAccessRecordUpdateRequest, responses={status.HTTP_200_OK: HikCentralAccessRecordSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=HikCentralAccessRecordUpdateRequest(data=request.data))
            record = self.hikcentral_access_record_repository.update_record(record_id=pk, record_data=update_data)
            if record is None:
                raise NotFound(detail="Record not found")
            else:
                return SuccessResponse(data_=HikCentralAccessRecordSerializer(record).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        record = self.hikcentral_access_record_repository.get_record(record_id=pk)
        deleted = self.hikcentral_access_record_repository.soft_delete_record(record_id=pk)
        if deleted is None:
            raise NotFound(detail="Record not found")
        else:
            return SuccessResponse(data_=HikCentralAccessRecordSerializer(record).data).send()