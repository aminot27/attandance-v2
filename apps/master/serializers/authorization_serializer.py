from rest_framework import serializers

from apps.master.models.profile_model import Profile
from apps.master.models.system_model import System
from apps.master.serializers.module_serializer import ModuleSerializer


class AuthorizationSerializer(serializers.ModelSerializer):
    systems = serializers.SerializerMethodField('get_systems')

    def __init__(self, *args):  # input a list of profiles
        super(AuthorizationSerializer, self).__init__(*args)

    def get_systems(self, profile):
        if 'systems' in profile.keys():
            return ProfileSystemSerializer(profile['systems'], many=True).data
        else:
            return []

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSystemSerializer(serializers.ModelSerializer):
    modules = serializers.SerializerMethodField('get_modules')

    def __init__(self, *args):  # input a list of systems
        super(ProfileSystemSerializer, self).__init__(*args)

    def get_modules(self, system):
        if 'modules' in system.keys():
            return ModuleSerializer(system['modules'], many=True).data
        else:
            return []

    class Meta:
        model = System
        fields = '__all__'
