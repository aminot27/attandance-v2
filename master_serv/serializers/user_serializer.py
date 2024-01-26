from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions')
