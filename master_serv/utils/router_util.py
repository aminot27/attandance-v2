class Route(object):
    def get_db_name(self, model):
        try:
            print(model)
            url = str(model.__module__).split(".")
            for n, i in enumerate(url):
                if i == "models":
                    url[n] = "setting"
            return '.'.join(url)
        except:
            return None

    def db_for_read(self, model, **hints):
        """
        Attempts to read historic models go to historical.
        """
        try:
            # mod = importlib.import_module(self.getNameDB(model))
            # database = getattr(mod, 'db_app')
            # ex
            app_name = 'default'
            # (Modificar instruccion para agregar nuevas DB)
            # elif model._meta.app_label == 'other_app_name':
            #    return 'other_app_name'
            return app_name
        except:
            return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write historic models go to historical.
        """
        try:
            app_name = 'default'
            # (Modificar instruccion para agregar nuevas DB)
            # elif model._meta.app_label == 'other_app_name':
            #    return 'other_app_name'
            return app_name
        except:
            return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the historic app is involved.
        """
        # if obj1._meta.app_label == 'cpip' or \
        #         obj2._meta.app_label == 'cpip':
        #     return True
        # return None
        db_list = ('default')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the historic app only appears in the 'historical' database.
        """
        if app_label == 'default':
            return db == 'default'
        return None
