from apps.warehouse.models.HikCentralAccessRecord_model import  HikCentralAccessRecord

class HikCentralAccessRecordRepository:
    @staticmethod
    def get_record(record_id):
        # Asume que existe un método get_one similar al de Shift
        return HikCentralAccessRecord.objects.get_one(record_id)

    @staticmethod
    def get_records(*values, **params):
        # Utiliza filter para obtener múltiples registros basados en parámetros
        return HikCentralAccessRecord.objects.filter(*values, **params)

    @staticmethod
    def post_records(*values, **params):
        # Este método parece ser un error en el nombre ya que post usualmente se refiere a crear
        # Suponiendo que se refiere a obtener muchos basado en parámetros específicos
        return HikCentralAccessRecord.objects.get_many(*values, **params)

    @staticmethod
    def create_record(record_data):
        # Crea un nuevo registro de acceso
        return HikCentralAccessRecord.objects.create_one(**record_data)

    @staticmethod
    def update_record(record_id, record_data):
        # Actualiza un registro de acceso existente
        return HikCentralAccessRecord.objects.update_one(obj_primary_key=record_id, **record_data)

    @staticmethod
    def log_delete_record(record_id):
        # Logica para registrar la eliminación de un registro, asumiendo una operación similar a Shift
        return HikCentralAccessRecord.objects.log_delete_one(primary_key=record_id)

    @staticmethod
    def soft_delete_record(record_id):
        # Eliminación suave de un registro, asumiendo una operación similar a Shift
        return HikCentralAccessRecord.objects.soft_delete_one(primary_key=record_id)