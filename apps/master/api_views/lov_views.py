import traceback

from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError, NotFound
from rest_framework.permissions import IsAuthenticated

from apps.master.serializers.LovSerializer import LovSerializer, LovDynamicResponse, LovCreateRequest, LovUpdateRequest
from master_serv.serializers.boolean_serializer import BooleanResponse
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView
from apps.master.repositories.lov_repository import LovRepository


class LovsView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={status.HTTP_200_OK: LovSerializer(many=True)})
    def get(self, request):
        try:
            lovs = LovRepository.get_lovs()
            return SuccessResponse(data_=LovSerializer(lovs, many=True).data).send()
        except APIException:
            tb = traceback.format_exc()
            print(tb)
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: LovDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request=request)
        lovs = LovRepository().get_lovs(*values, **params)
        if type(lovs) is FieldError:
            raise ValidationError(lovs)
        return SuccessResponse(data_=LovDynamicResponse(lovs, many=True, fields=values).data).send()


class LovView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=LovCreateRequest,
                         responses={status.HTTP_200_OK: LovSerializer()})
    def post(self, request):
        create_data = super().get_request_data(LovCreateRequest(data=request.data))
        try:
            lov = LovRepository().create_lov(create_data)
            return SuccessResponse(data_=LovSerializer(lov).data).send()
        except:
            raise APIException(detail='Error creating lov')


class LovDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={status.HTTP_200_OK: LovSerializer()})
    def get(self, request, pk):
        lov = LovRepository().get_lov(lov_id=pk)
        if lov is None:
            raise NotFound(detail='Lov not found')
        return SuccessResponse(data_=LovSerializer(lov).data).send()

    @swagger_auto_schema(request_body=LovUpdateRequest,
                         responses={status.HTTP_200_OK: LovSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=LovUpdateRequest(data=request.data))
            lov = LovRepository().update_lov(lov_id=pk, lov=update_data)
            if lov is None:
                raise NotFound(detail='Lov not found')
            return SuccessResponse(data_=LovSerializer(lov).data).send()
        except:
            tb = traceback.format_exc()
            print(tb)
            raise APIException()

    @swagger_auto_schema(responses={status.HTTP_200_OK: BooleanResponse()})
    def delete(self, request, pk):
        if LovRepository().delete_lov(lov_id=pk) is None:
            raise NotFound(detail='Lov not found')
        return SuccessResponse(data_=BooleanResponse({'processed': True}).data).send()
