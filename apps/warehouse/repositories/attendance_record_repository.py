from apps.warehouse.models.attendance_record_model import AttendanceRecord

class AttendanceRecordRepository:
    @staticmethod
    def get_attendance_record(attendance_id):
        return AttendanceRecord.objects.get_one(attendance_id)

    @staticmethod
    def get_attendance_records(*values, **params):
        return AttendanceRecord.objects.filter(*values, **params)

    @staticmethod
    def post_attendance_records(*values, **params):
        return AttendanceRecord.objects.get_many(*values, **params)

    @staticmethod
    def create_attendance_record(attendance_data):
        return AttendanceRecord.objects.create_one(**attendance_data)

    @staticmethod
    def update_attendance_record(attendance_id, attendance_data):
        return AttendanceRecord.objects.update_one(obj_primary_key=attendance_id, **attendance_data)

    @staticmethod
    def log_delete_attendance_record(attendance_id):
        return AttendanceRecord.objects.log_delete_one(primary_key=attendance_id)

    @staticmethod
    def soft_delete_attendance_record(attendance_id):
        return AttendanceRecord.objects.soft_delete_one(primary_key=attendance_id)