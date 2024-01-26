import os
import traceback
from django.core.mail import send_mail, EmailMultiAlternatives, BadHeaderError
from django.template import loader
from django.contrib.auth.base_user import BaseUserManager

FROM = '"SESPO" <construinnovaperu@gmail.com>'


class MailFactory:
    @staticmethod
    def send_reset_password_mail(_username=None, _email=None, _new_password=None):
        try:
            template_path = os.path.join('master_serv', 'utils', 'templates', 'reset_password_template.html')
            template = loader.get_template(template_path)
            context = {
                'username': _username,
                'new_password': _new_password
            }
            render = template.render(context)
            to = [_email]
            msg = EmailMultiAlternatives('Contraseña Reestablecida', render, FROM, to)
            msg.attach_alternative(render, 'text/html')
            msg.send()
            return "OK"
        except Exception as e:
            tb = traceback.format_exc()
            # print(tb)
            return str(e)
