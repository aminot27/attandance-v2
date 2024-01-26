from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException, NotFound, ValidationError

from apps.warehouse.models.academy_model import Academy
from apps.warehouse.repositories.academy_repository import AcademyRepository
from apps.warehouse.serializers.academy_serializers import (
    AcademySerializer,
    AcademyDynamicResponse,
    AcademyCreateRequest,
    AcademyUpdateRequest
)
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView

class AcademiesView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    academy_repository = AcademyRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: AcademySerializer(many=True)})
    def get(self, request):
        try:
            academies = self.academy_repository.get_academies()
            return SuccessResponse(data_=AcademySerializer(academies, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: AcademyDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        academies = self.academy_repository.post_academies(*values, **params)
        if type(academies) is FieldError:
            raise ValidationError(academies)
        else:
            return SuccessResponse(
                data_=AcademyDynamicResponse(academies, many=True, fields=values).data).send()

class AcademyView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    academy_repository = AcademyRepository()

    @swagger_auto_schema(request_body=AcademyCreateRequest, responses={status.HTTP_200_OK: AcademySerializer()})
    def post(self, request):
        create_data = super().get_request_data(AcademyCreateRequest(data=request.data))
        try:
            academy = self.academy_repository.create_academy(create_data)
            return SuccessResponse(data_=AcademySerializer(academy).data).send()
        except:
            raise APIException(detail="Error creating academy")

class AcademyDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    academy_repository = AcademyRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: AcademySerializer()})
    def get(self, request, pk):
        academy = self.academy_repository.get_academy(academy_id=pk)
        if academy is None:
            raise NotFound(detail="Academy not found")
        else:
            return SuccessResponse(data_=AcademySerializer(academy).data).send()

    @swagger_auto_schema(request_body=AcademyUpdateRequest, responses={status.HTTP_200_OK: AcademySerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=AcademyUpdateRequest(data=request.data))
            academy = self.academy_repository.update_academy(academy_id=pk, academy=update_data)
            if academy is None:
                raise NotFound(detail="Academy not found")
            else:
                return SuccessResponse(data_=AcademySerializer(academy).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        academy = self.academy_repository.get_academy(academy_id=pk)
        deleted = self.academy_repository.soft_delete_academy(academy_id=pk)
        if deleted is None:
            raise NotFound(detail="Academy not found")
        else:
            return SuccessResponse(data_=AcademySerializer(academy).data).send()