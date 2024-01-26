from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException, NotFound, ValidationError

from apps.warehouse.models.location_record_model import LocationRecord
from apps.warehouse.repositories.location_record_repository import LocationRecordRepository
from apps.warehouse.serializers.location_record_serializers import (
    LocationRecordSerializer,
    LocationRecordDynamicResponse,
    LocationRecordCreateRequest,
    LocationRecordUpdateRequest
)
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView

class LocationRecordsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    location_record_repository = LocationRecordRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: LocationRecordSerializer(many=True)})
    def get(self, request):
        try:
            location_records = self.location_record_repository.get_location_records()
            return SuccessResponse(data_=LocationRecordSerializer(location_records, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: LocationRecordDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        location_records = self.location_record_repository.post_location_records(*values, **params)
        if type(location_records) is FieldError:
            raise ValidationError(location_records)
        else:
            return SuccessResponse(
                data_=LocationRecordDynamicResponse(location_records, many=True, fields=values).data).send()

class LocationRecordView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    location_record_repository = LocationRecordRepository()

    @swagger_auto_schema(request_body=LocationRecordCreateRequest, responses={status.HTTP_200_OK: LocationRecordSerializer()})
    def post(self, request):
        create_data = super().get_request_data(LocationRecordCreateRequest(data=request.data))
        try:
            location_record = self.location_record_repository.create_location_record(create_data)
            return SuccessResponse(data_=LocationRecordSerializer(location_record).data).send()
        except:
            raise APIException(detail="Error creating location record")

class LocationRecordDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    location_record_repository = LocationRecordRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: LocationRecordSerializer()})
    def get(self, request, pk):
        location_record = self.location_record_repository.get_location_record(location_id=pk)
        if location_record is None:
            raise NotFound(detail="Location record not found")
        else:
            return SuccessResponse(data_=LocationRecordSerializer(location_record).data).send()

    @swagger_auto_schema(request_body=LocationRecordUpdateRequest, responses={status.HTTP_200_OK: LocationRecordSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=LocationRecordUpdateRequest(data=request.data))
            location_record = self.location_record_repository.update_location_record(location_id=pk, location_record=update_data)
            if location_record is None:
                raise NotFound(detail="Location record not found")
            else:
                return SuccessResponse(data_=LocationRecordSerializer(location_record).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        location_record = self.location_record_repository.get_location_record(location_id=pk)
        deleted = self.location_record_repository.soft_delete_location_record(location_id=pk)
        if deleted is None:
            raise NotFound(detail="Location record not found")
        else:
            return SuccessResponse(data_=LocationRecordSerializer(location_record).data).send()