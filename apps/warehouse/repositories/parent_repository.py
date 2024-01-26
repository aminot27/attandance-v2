from apps.warehouse.models.parent_model import Parent

class ParentRepository:

    @staticmethod
    def get_parent(parent_id):
        return Parent.objects.get_one(parent_id)

    @staticmethod
    def get_parents(*values, **params):
        return Parent.objects.filter(*values, **params)

    @staticmethod
    def post_parents(*values, **params):
        return Parent.objects.get_many(*values, **params)

    @staticmethod
    def create_parent(parent_data):
        return Parent.objects.create_one(**parent_data)

    @staticmethod
    def update_parent(parent_id, parent_data):
        return Parent.objects.update_one(obj_primary_key=parent_id, **parent_data)

    @staticmethod
    def log_delete_parent(parent_id):
        return Parent.objects.log_delete_one(primary_key=parent_id)

    @staticmethod
    def soft_delete_parent(parent_id):
        return Parent.objects.soft_delete_one(primary_key=parent_id)