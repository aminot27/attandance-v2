from rest_framework import serializers
from apps.master.models.system_user_model import SystemUser


class SystemUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = '__all__'


class SystemUserRequest(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = SystemUser
        # dni,first name,last name, entity, email, pswd, mobile_user_id
        exclude = ('auth_user', 'document_type', 'status')


from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer
from master_serv.serializers.user_serializer import UserSerializer


class SystemUserResponse(DynamicFieldsModelSerializer):
    auth_user = UserSerializer()

    class Meta:
        model = SystemUser
        exclude = ('document_type', 'status')


class SystemUserFreeRegisterRequest(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = SystemUser
        exclude = ('auth_user', 'status')


class DocumentRequest(serializers.Serializer):
    document = serializers.CharField(max_length=8)


class ChangePasswordRequest(serializers.Serializer):
    document = serializers.CharField(max_length=8)
    password = serializers.CharField()
    new_password = serializers.CharField()
