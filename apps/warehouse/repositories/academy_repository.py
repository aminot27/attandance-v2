from apps.warehouse.models.academy_model import Academy

class AcademyRepository:

    @staticmethod
    def get_academy(academy_id):
        return Academy.objects.get_one(academy_id)

    @staticmethod
    def get_academies(*values, **params):
        return Academy.objects.filter(*values, **params)

    @staticmethod
    def post_academies(*values, **params):
        return Academy.objects.get_many(*values, **params)

    @staticmethod
    def create_academy(academy):
        return Academy.objects.create_one(**academy)

    @staticmethod
    def update_academy(academy_id, academy):
        return Academy.objects.update_one(obj_primary_key=academy_id, **academy)

    @staticmethod
    def log_delete_academy(academy_id):
        return Academy.objects.log_delete_one(primary_key=academy_id)

    @staticmethod
    def soft_delete_academy(academy_id):
        return Academy.objects.soft_delete_one(primary_key=academy_id)