from twilio.rest import Client
from django.utils.timezone import localtime
# Asegúrate de importar el modelo Student
from apps.warehouse.models.student_model import Student

def sendSms(student_dni, action, time, status):
    account_sid = 'ACbc58ad6b0a5ac0c5e6964881275e4cbe'
    auth_token = 'cc9ae90856073abffeabcce3c0278f2a'
    client = Client(account_sid, auth_token)

    try:
        # Buscar el estudiante por DNI para obtener el objeto Student
        student = Student.objects.get(dni=student_dni)
        parent_phone_number = student.parent.phone_number  # Acceder al número de teléfono del padre
    except Student.DoesNotExist:
        print("Estudiante no encontrado")
        return

    # Personalizar el mensaje basado en la acción
    if action == "entry":
        body_message = f"Hola {student.name},\nhas marcado tu entrada a las {time}.\nEstado: {status}"
    elif action == "exit":
        body_message = f"Hola {student.name},\nhas marcado tu salida a las {time}.\n"
    else:
        body_message = "Acción no reconocida."

    # Enviar el mensaje al número de teléfono del padre
    message = client.messages.create(
        from_='+16592175883',
        body=body_message,
        to=f'+51{parent_phone_number}'  # Asegúrate de incluir el código de país si es necesario
    )

    print(message.sid)