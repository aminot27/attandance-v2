from apps.master.models.lov_model import Lov


class LovRepository:
    @staticmethod
    def get_lov(lov_id):
        return Lov.objects.get_one(obj_primary_key=lov_id)

    @staticmethod
    def get_lovs(*values, **params):
        return Lov.objects.get_many(*values, **params)

    @staticmethod
    def create_lov(lov):
        return Lov.objects.create_one(**lov)

    @staticmethod
    def update_lov(lov_id, lov):
        return Lov.objects.update_one(obj_primary_key=lov_id, **lov)

    @staticmethod
    def delete_lov(lov_id):
        return Lov.objects.soft_delete_one(primary_key=lov_id)
