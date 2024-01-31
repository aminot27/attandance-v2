from apps.warehouse.models.student_model import Student

class StudentRepository:
    @staticmethod
    def get_student(student_id):
        return Student.objects.get_one(student_id)

    @staticmethod
    def get_students(*values, **params):
        return Student.objects.filter(*values, **params)

    @staticmethod
    def post_students(*values, **params):
        return Student.objects.get_many(*values, **params)

    @staticmethod
    def create_student(student_data):
        return Student.objects.create_one(**student_data)

    @staticmethod
    def update_student(student_id, student):
        return Student.objects.update_one(obj_primary_key=student_id, **student)

    @staticmethod
    def log_delete_student(student_id):
        return Student.objects.log_delete_one(primary_key=student_id)

    @staticmethod
    def soft_delete_student(student_id):
        return Student.objects.soft_delete_one(primary_key=student_id)