from rest_framework import status

import json
from datetime import datetime as datetime4token
from datetime import timedelta as timedelta4token
import jwt
import traceback
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from apps.master.models.system_user_model import SystemUser
from .response_util import Resp
from ..settings.base_setting import SECRET_KEY


class TokenJWTBasicAuth:
    def __init__(self):
        self.TOKEN_SECRET_SERV = 'TOKENSECRETKEY'

    def create_token(self, user):
        try:
            payload = {
                'sub': user,
                'iat': datetime4token.utcnow(),
                'exp': datetime4token.utcnow() + timedelta4token(minutes=30)
            }
            token = jwt.encode(payload, self.TOKEN_SECRET_SERV, algorithm='HS256').decode('UTF-8')
            return token
        except:
            tb = traceback.format_exc()
            print(tb)
            return None

    @csrf_exempt
    def authenticate(request):
        try:
            body = request.body.decode('utf-8')
            data = json.loads(body)
            username = data["username"]
            passwd = data["password"].encode()
            #
            result = authenticate(username=username, password=passwd)
            #
            if result is not None:
                #
                data['token'] = TokenJWTBasicAuth().create_token(data["username"])
                ## return Resp(True, "Loggin Success", {"token": data["token"]}, code_=200).send()
                return HttpResponse(json.dumps({"token": data["token"]}), content_type="application/json")
            else:
                return Resp(False, "Logging Failed", None, code_=401).send()
                # return HttpResponse(json.dumps({'msg': 'Nombre de usuario o contraseña incorrecto'}), status=401)
        except:
            tb = traceback.format_exc()
            print(tb)
            return Resp(False, "Internal Error", None, code_=500).send()

    def get_sub(self, request):

        if 'HTTP_AUTHORIZATION' not in request.META:
            retorno = Resp(False, "Unauthorized!!!", None, code_=401)
            retorno.send()
            return None
        try:
            token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
            payload = jwt.decode(token, self.TOKEN_SECRET_SERV, algorithms=['HS256'])
            return payload['sub']
        except:
            tb = traceback.format_exc()
            return Resp(False, "Internal Error", None, code_=500).send()


class TokenSimpleJWTAuth:
    """
    return
    user_id: if token is decoded
    -1: if HTTP_AUTHORIZATION is not in request.META
    0: if catch exception
    """

    def get_user_id_from_request(self, request):

        if 'HTTP_AUTHORIZATION' not in request.META:
            return -1
        try:
            token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return payload['user_id']
        except:
            tb = traceback.format_exc()
            print(tb)
            return 0

    def get_user_id_from_token(self, token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return payload['user_id']
        except:
            tb = traceback.format_exc()
            print(tb)
            return 'error decoding token'
