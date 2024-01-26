from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException, NotFound, ValidationError

from apps.warehouse.models.student_model import Student
from apps.warehouse.repositories.student_repository import StudentRepository
from apps.warehouse.serializers.student_serializers import (
    StudentSerializer,
    StudentDynamicResponse,
    StudentCreateRequest,
    StudentUpdateRequest
)
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView

class StudentsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    student_repository = StudentRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: StudentSerializer(many=True)})
    def get(self, request):
        try:
            students = self.student_repository.get_students()
            return SuccessResponse(data_=StudentSerializer(students, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: StudentDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        students = self.student_repository.post_students(*values, **params)
        if type(students) is FieldError:
            raise ValidationError(students)
        else:
            return SuccessResponse(
                data_=StudentDynamicResponse(students, many=True, fields=values).data).send()

class StudentView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    student_repository = StudentRepository()

    @swagger_auto_schema(request_body=StudentCreateRequest, responses={status.HTTP_200_OK: StudentSerializer()})
    def post(self, request):
        create_data = super().get_request_data(StudentCreateRequest(data=request.data))
        try:
            student = self.student_repository.create_student(create_data)
            return SuccessResponse(data_=StudentSerializer(student).data).send()
        except:
            raise APIException(detail="Error creating student")

class StudentDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    student_repository = StudentRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: StudentSerializer()})
    def get(self, request, pk):
        student = self.student_repository.get_student(student_id=pk)
        if student is None:
            raise NotFound(detail="Student not found")
        else:
            return SuccessResponse(data_=StudentSerializer(student).data).send()

    @swagger_auto_schema(request_body=StudentUpdateRequest, responses={status.HTTP_200_OK: StudentSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=StudentUpdateRequest(data=request.data))
            student = self.student_repository.update_student(student_id=pk, student=update_data)
            if student is None:
                raise NotFound(detail="Student not found")
            else:
                return SuccessResponse(data_=StudentSerializer(student).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        student = self.student_repository.get_student(student_id=pk)
        deleted = self.student_repository.soft_delete_student(student_id=pk)
        if deleted is None:
            raise NotFound(detail="Student not found")
        else:
            return SuccessResponse(data_=StudentSerializer(student).data).send()

