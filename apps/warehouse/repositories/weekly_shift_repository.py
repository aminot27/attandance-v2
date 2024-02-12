from apps.warehouse.models.shift_model import Shift
from apps.warehouse.models.weekly_shift_model import WeeklyShift  # Asegúrate de importar correctamente el modelo WeeklyShift

class WeeklyShiftRepository:
    @staticmethod
    def get_weekly_shift(weekly_shift_id):
        # Asumiendo que existe un método similar a get_one en el modelo WeeklyShift
        return WeeklyShift.objects.get_one(weekly_shift_id)

    @staticmethod
    def get_weekly_shifts(*values, **params):
        return WeeklyShift.objects.filter(*values, **params)

    @staticmethod
    def post_weekly_shifts(*values, **params):
        # Asumiendo que existe un método similar a get_many en el modelo WeeklyShift
        return WeeklyShift.objects.get_many(*values, **params)

    @staticmethod
    def create_weekly_shift(weekly_shift_data):
        # Asumiendo que existe un método similar a create_one en el modelo WeeklyShift
        return WeeklyShift.objects.create_one(**weekly_shift_data)

    @staticmethod
    def update_weekly_shift(weekly_shift_id, weekly_shift_data):
        # Asumiendo que existe un método similar a update_one en el modelo WeeklyShift
        return WeeklyShift.objects.update_one(obj_primary_key=weekly_shift_id, **weekly_shift_data)

    @staticmethod
    def log_delete_weekly_shift(weekly_shift_id):
        # Asumiendo que existe un método similar a log_delete_one en el modelo WeeklyShift
        return WeeklyShift.objects.log_delete_one(primary_key=weekly_shift_id)

    @staticmethod
    def soft_delete_weekly_shift(weekly_shift_id):
        # Asumiendo que existe un método similar a soft_delete_one en el modelo WeeklyShift
        return WeeklyShift.objects.soft_delete_one(primary_key=weekly_shift_id)