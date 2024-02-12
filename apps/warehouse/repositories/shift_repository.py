from apps.warehouse.models.shift_model import Shift

class ShiftRepository:
    @staticmethod
    def get_shift(shift_id):
        return Shift.objects.get_one(shift_id)

    @staticmethod
    def get_shifts(*values, **params):
        return Shift.objects.filter(*values, **params)

    @staticmethod
    def post_shifts(*values, **params):
        return Shift.objects.get_many(*values, **params)

    @staticmethod
    def create_shift(shift_data):
        return Shift.objects.create_one(**shift_data)

    @staticmethod
    def update_shift(shift_id, shift):
        return Shift.objects.update_one(obj_primary_key=shift_id, **shift)

    @staticmethod
    def log_delete_shift(shift_id):
        return Shift.objects.log_delete_one(primary_key=shift_id)

    @staticmethod
    def soft_delete_shift(shift_id):
        return Shift.objects.soft_delete_one(primary_key=shift_id)