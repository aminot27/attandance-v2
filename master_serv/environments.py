import json
import sys
import os


class Environments:

    def load_environment(self, apps_names, is_lite_db):
        from master_serv.settings.base_setting import ROOT_DIR
        db_conf = {}
        if is_lite_db:
            db_conf = {
                apps_names[0]: {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': str(ROOT_DIR / 'db.sqlite3'),
                }
            }
        else:
            env_file = str(ROOT_DIR / 'environment.json')
            with open(str(ROOT_DIR / 'env.json')) as data_file:
                env = json.load(data_file)
            if env['DEBUG'] is False:
                env_file = str(ROOT_DIR / 'environment.prod.json')
            with open(env_file) as data_file:
                config = json.load(data_file)

            for app_name in apps_names:
                db_conf[app_name] = {
                    'ENGINE': str(config[app_name]['ENGINE']),
                    'HOST': str(config[app_name]['HOST']),
                    'PORT': str(config[app_name]['PORT']),
                    'NAME': str(config[app_name]['NAME']),
                    'USER': str(config[app_name]['USER']),
                    'PASSWORD': str(config[app_name]['PASSWORD'])
                }
            # print(db_conf)
        return db_conf
