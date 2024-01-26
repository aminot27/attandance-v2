from apps.warehouse.models.location_record_model import LocationRecord

class LocationRecordRepository:

    @staticmethod
    def get_location_record(location_id):
        return LocationRecord.objects.get_one(location_id)

    @staticmethod
    def get_location_records(*values, **params):
        return LocationRecord.objects.filter(*values, **params)

    @staticmethod
    def post_location_records(*values, **params):
        return LocationRecord.objects.get_many(*values, **params)

    @staticmethod
    def create_location_record(location_record):
        return LocationRecord.objects.create_one(**location_record)

    @staticmethod
    def update_location_record(location_id, location_record):
        return LocationRecord.objects.update_one(obj_primary_key=location_id, **location_record)

    @staticmethod
    def log_delete_location_record(location_id):
        return LocationRecord.objects.log_delete_one(primary_key=location_id)

    @staticmethod
    def soft_delete_location_record(location_id):
        return LocationRecord.objects.soft_delete_one(primary_key=location_id)