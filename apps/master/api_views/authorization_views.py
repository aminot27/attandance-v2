import traceback

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.master.models.module_model import Module
from apps.master.models.profile_model import Profile
from apps.master.models.system_model import System
from apps.master.models.system_user_model import SystemUser
from apps.master.serializers.authorization_serializer import AuthorizationSerializer
from master_serv.models.model_status import MODEL_STATUS_INACTIVE, MODEL_STATUS_ACTIVE
from master_serv.utils.error_response import ErrorResponse
from master_serv.utils.response_util import ToJson
from master_serv.utils.success_response import SuccessResponse
from master_serv.utils.token_auth_util import TokenSimpleJWTAuth


class AuthorizationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user_authorizations = []
            user_id = TokenSimpleJWTAuth().get_user_id_from_request(request)
            try:
                system_user = SystemUser.objects.get(auth_user_id=user_id)
                if system_user.status == MODEL_STATUS_ACTIVE:
                    profiles = Profile.objects.filter(systemuserprofile__system_user_id=system_user.system_user_id)
                    for profile in profiles:
                        systems_list = []
                        profile_dict = ToJson().data_json(profile)
                        systems = System.objects.filter(
                            module__access__profile_id=profile.profile_id).distinct('system_id')
                        for system in systems:
                            system_dict = ToJson().data_json(system)
                            system_dict['modules'] = Module.objects.filter(system_id=system.system_id,
                                                                           access__profile_id=profile.profile_id) \
                                .order_by('order')
                            systems_list.append(system_dict)
                        profile_dict['systems'] = systems_list
                        user_authorizations.append(profile_dict)
                    return SuccessResponse(data_=AuthorizationSerializer(user_authorizations, many=True).data,
                                           msg_='Authorization successfully').send()
                else:
                    return ErrorResponse(msg_='This user is not active').send_bad_request()
            except SystemUser.DoesNotExist:
                return ErrorResponse(msg_='System user not found for this user account').send_not_found()


        except:
            tb = traceback.format_exc()
            print(tb)
            return ErrorResponse().send_internal_server_error()
