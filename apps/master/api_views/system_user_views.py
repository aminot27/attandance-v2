import traceback
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User
from django.core.exceptions import FieldError
from django.db import transaction, DatabaseError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from apps.master.models.system_user_model import SystemUser
from apps.master.serializers.system_serializer import SystemUserFreeRegisterRequest, SystemUserResponse, \
    DocumentRequest, ChangePasswordRequest, SystemUserRequest, SystemUserSerializer
from master_serv.models.model_status import MODEL_STATUS_CREATED, MODEL_STATUS_DELETED
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.email.email_factory import MailFactory
from django.contrib.auth import authenticate

from master_serv.utils.error_response import ErrorResponse
from master_serv.utils.success_response import SuccessResponse


class SystemUserRegister(APIView):
    permission_classes = []

    @swagger_auto_schema(request_body=SystemUserFreeRegisterRequest,
                         responses={status.HTTP_200_OK: SystemUserResponse()})
    def post(self, request):
        try:
            register_request = SystemUserFreeRegisterRequest(data=request.data)
            if register_request.is_valid():
                document = register_request.data['document']
                gender = register_request.data['gender']
                phone = register_request.data['phone']
                entity = register_request.data['entity']
                avatar = register_request.data['avatar']
                first_name = register_request.data['first_name']
                last_name = register_request.data['last_name']
                email = register_request.data['email']
                password = register_request.data['password']
                try:
                    with transaction.atomic():
                        auth_user = User.objects.create_user(email=email, username=email, first_name=first_name,
                                                             last_name=last_name, password=password)
                        system_user = SystemUser.objects.create(auth_user=auth_user, document_type='DNI',
                                                                document=document, gender=gender,
                                                                phone=phone, entity=entity, avatar=avatar,
                                                                status=MODEL_STATUS_CREATED)
                        system_user_serializer_response = SystemUserResponse(system_user)
                except DatabaseError as ex:
                    return ErrorResponse(msg_=str(ex)).send_bad_request()
                return SuccessResponse(data_=system_user_serializer_response.data,
                                       msg_="User registered successfully").send()
            else:
                return ErrorResponse(data_=register_request.errors, msg_='Error registering user').send_bad_request()
        except:
            tb = traceback.format_exc()
            print(tb)
            return ErrorResponse().send_internal_server_error()


class ResetPassword(APIView):
    permission_classes = []

    @swagger_auto_schema(request_body=DocumentRequest)
    def post(self, request):
        try:
            document_request = DocumentRequest(data=request.data)
            if document_request.is_valid():
                document = document_request.data['document']
                auth_user = User.objects.get(username=document)
                new_password = BaseUserManager().make_random_password()
                auth_user.set_password(new_password)
                auth_user.save()
                email_status = MailFactory.send_reset_password_mail(_username=auth_user.first_name,
                                                                    _email=auth_user.email,
                                                                    _new_password=new_password)
                return SuccessResponse(msg_=email_status).send()
            else:
                return ErrorResponse(data_=document_request.errors, msg_='Reset password error').send_bad_request()
        except:
            tb = traceback.format_exc()
            print(tb)
            return ErrorResponse().send_internal_server_error()


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ChangePasswordRequest)
    def post(self, request):
        try:
            change_request = ChangePasswordRequest(data=request.data)
            if change_request.is_valid():
                document = change_request.data['document']
                password = change_request.data['password']
                new_password = change_request.data['new_password']
                auth = authenticate(username=document, password=password)
                if auth is not None:
                    auth_user = User.objects.get(username=document)
                    auth_user.set_password(new_password)
                    auth_user.save()
                    return SuccessResponse(msg_="Password was change successfully").send()
                else:
                    return ErrorResponse(msg_='Username or password is incorrect').send_unauthorized()
            else:
                return ErrorResponse(data_=change_request.errors,
                                     msg_='Change password params error').send_bad_request()
        except:
            tb = traceback.format_exc()
            print(tb)
            return ErrorResponse().send_internal_server_error()


class SystemUsersView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: SystemUserResponse(many=True)})
    def post(self, request):
        try:
            filter_request = FilterRequestFormatSerializer(data=request.data)
            if filter_request.is_valid():
                params = filter_request.data['params']
                values = filter_request.data['values']
                try:
                    system_users = SystemUser.objects.filter(**params)
                    filter_response = SystemUserResponse(system_users, many=True, fields=values)
                    return SuccessResponse(data_=filter_response.data).send()
                except FieldError as err:
                    return ErrorResponse(msg_=str(err)).send_bad_request()

            else:
                return ErrorResponse(msg_='Invalid filter params', data_=filter_request.errors).send_bad_request()
        except:
            tb = traceback.format_exc()
            print(tb)
            return ErrorResponse().send_internal_server_error()


class SystemUserView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=SystemUserRequest,
                         responses={status.HTTP_200_OK: SystemUserResponse()})
    def post(self, request):
        try:
            system_user_request = SystemUserRequest(data=request.data)
            if system_user_request.is_valid():
                document = system_user_request.data['document']
                gender = system_user_request.data['gender']
                phone = system_user_request.data['phone']
                entity = system_user_request.data['entity']
                avatar = system_user_request.data['avatar']
                first_name = system_user_request.data['first_name']
                last_name = system_user_request.data['last_name']
                email = system_user_request.data['email']
                password = document + '0'
                try:
                    with transaction.atomic():
                        auth_user = User.objects.create_user(email=email, username=email, first_name=first_name,
                                                             last_name=last_name, password=password)
                        system_user = SystemUser.objects.create(auth_user=auth_user, document_type='DNI',
                                                                document=document, gender=gender,
                                                                phone=phone, entity=entity, avatar=avatar,
                                                                status=MODEL_STATUS_CREATED)
                        system_user_serializer_response = SystemUserResponse(system_user)
                except DatabaseError as ex:
                    return ErrorResponse(msg_=str(ex)).send_bad_request()
                return SuccessResponse(data_=system_user_serializer_response.data,
                                       msg_="User created successfully").send()
            else:
                return ErrorResponse(data_=system_user_request.errors, msg_='Error creating user').send_bad_request()
        except:
            tb = traceback.format_exc()
            print(tb)
            return ErrorResponse().send_internal_server_error()

    @swagger_auto_schema(responses={status.HTTP_200_OK: SystemUserResponse()})
    def get(self, request, pk):
        try:
            system_user = SystemUser.objects.get(system_user_id=pk)
            system_user_response = SystemUserResponse(system_user)
            return SuccessResponse(data_=system_user_response.data).send()
        except SystemUser.DoesNotExist:
            return ErrorResponse(msg_='System user not found').send_not_found()

    @swagger_auto_schema(request_body=SystemUserSerializer, responses={status.HTTP_200_OK: SystemUserResponse()})
    def put(self, request, pk):
        try:
            system_user = SystemUser.objects.get(system_user_id=pk)
            system_user_request = SystemUserSerializer(system_user, data=request.data, partial=True)
            if system_user_request.is_valid():
                system_user_request.save()
                return SuccessResponse(msg_='System user updated successfully').send()
            else:
                return ErrorResponse(data_=system_user_request.errors,
                                     msg_='Error updating system user').send_bad_request()
        except SystemUser.DoesNotExist:
            return ErrorResponse(msg_='System user not fount').send_not_found()

    def delete(self, request, pk):
        try:
            system_user = SystemUser.objects.get(system_user_id=pk)
            system_user.status = MODEL_STATUS_DELETED

        except SystemUser.DoesNotExist:
            return ErrorResponse(msg_='System user not found').send_not_found()
