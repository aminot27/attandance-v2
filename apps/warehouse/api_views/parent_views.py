import traceback

from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException, NotFound, ValidationError

from apps.warehouse.models.parent_model import Parent
from apps.warehouse.repositories.parent_repository import ParentRepository
from apps.warehouse.serializers.parent_serializers import (
    ParentSerializer,
    ParentDynamicResponse,
    ParentCreateRequest,
    ParentUpdateRequest
)
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView

class ParentsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    parent_repository = ParentRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: ParentSerializer(many=True)})
    def get(self, request):
        try:
            parents = self.parent_repository.get_parents()
            return SuccessResponse(data_=ParentSerializer(parents, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: ParentDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        parents = self.parent_repository.post_parents(*values, **params)
        if type(parents) is FieldError:
            raise ValidationError(parents)
        else:
            return SuccessResponse(
                data_=ParentDynamicResponse(parents, many=True, fields=values).data).send()

class ParentView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    parent_repository = ParentRepository()

    @swagger_auto_schema(request_body=ParentCreateRequest, responses={status.HTTP_200_OK: ParentSerializer()})
    def post(self, request):
        create_data = super().get_request_data(ParentCreateRequest(data=request.data))
        try:
            parent = self.parent_repository.create_parent(create_data)
            return SuccessResponse(data_=ParentSerializer(parent).data).send()
        except:
            raise APIException(detail="Error creating parent")

class ParentDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    parent_repository = ParentRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: ParentSerializer()})
    def get(self, request, pk):
        parent = self.parent_repository.get_parent(parent_id=pk)
        if parent is None:
            raise NotFound(detail="Parent not found")
        else:
            return SuccessResponse(data_=ParentSerializer(parent).data).send()

    @swagger_auto_schema(request_body=ParentUpdateRequest, responses={status.HTTP_200_OK: ParentSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=ParentUpdateRequest(data=request.data))
            parent = self.parent_repository.update_parent(parent_id=pk, parent=update_data)
            if parent is None:
                raise NotFound(detail="Parent not found")
            else:
                return SuccessResponse(data_=ParentSerializer(parent).data).send()
        except:
            tb = traceback.format_exc()
            print(tb)
            raise APIException()

    def delete(self, request, pk):
        parent = self.parent_repository.get_parent(parent_id=pk)
        deleted = self.parent_repository.soft_delete_parent(parent_id=pk)
        if deleted is None:
            raise NotFound(detail="Parent not found")
        else:
            return SuccessResponse(data_=ParentSerializer(parent).data).send()