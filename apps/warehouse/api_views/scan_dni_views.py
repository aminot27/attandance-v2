from django.utils.timezone import localtime, now
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from twilio.base.exceptions import TwilioRestException

from apps.warehouse.models.student_model import Student
from apps.warehouse.models.shift_model import Shift
from apps.warehouse.models.attendance_record_model import AttendanceRecord
from apps.warehouse.serializers.scan_dni_serializers import ScanDniRequestSerializer, AttendanceRecordDniSerializer
from master_serv.utils.success_response import SuccessResponse
from twilio.rest import Client
from django.utils.timezone import localtime, get_default_timezone

class ScanDniView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ScanDniRequestSerializer,
                         responses={status.HTTP_200_OK: AttendanceRecordDniSerializer()})
    def post(self, request):
        serializer = ScanDniRequestSerializer(data=request.data)
        if serializer.is_valid():
            dni = serializer.validated_data['dni']
            try:
                student = Student.objects.get(dni=dni)
            except Student.DoesNotExist:
                raise NotFound(detail="Estudiante no encontrado")
            now_time = localtime(now()).time()
            shifts = Shift.objects.all()
            current_shift = None
            for shift in shifts:
                if shift.start_time <= now_time <= shift.end_time:
                    current_shift = shift
                    break
            if not current_shift:
                return Response({
                    'message': 'No hay turnos activos en este momento o el estudiante no está asignado a ningún turno.'
                }, status=status.HTTP_200_OK)

            today_date = localtime(now()).date()
            try:
                attendance_record = AttendanceRecord.objects.get(
                    student=student,
                    shift=current_shift,
                    entry_time__date=today_date  # Filtra por la fecha de entry_time
                )
                created = False
            except AttendanceRecord.DoesNotExist:
                # Si no existe, crea un nuevo registro
                attendance_record = AttendanceRecord.objects.create(
                    student=student,
                    shift=current_shift,
                    status='Falta'  # Inicializa con 'Absent'
                )
                created = True

            # Verifica si el escaneo ocurre dentro del intervalo de salida
            if current_shift.leave_start and current_shift.leave_end and current_shift.leave_start <= now_time <= current_shift.leave_end:
                # Solo actualiza exit_time si el registro ya existe y el estudiante ya marcó entrada
                if not created and attendance_record.entry_time:
                    attendance_record.exit_time = localtime(now())
                    attendance_record.save()

            # Actualiza el estado si el registro es nuevo o el estudiante estaba marcado como ausente
            if created or attendance_record.status == 'Falta':
                # Verifica si el estudiante está marcado como 'Early'
                if current_shift.entry_start and current_shift.entry_end and current_shift.entry_start <= now_time <= current_shift.early_until:
                    attendance_record.status = 'Temprano'
                # Verifica si el estudiante está marcado como 'Late'
                elif current_shift.late_until and current_shift.early_until < now_time <= current_shift.late_until:
                    attendance_record.status = 'Tarde'
                attendance_record.save()

            student_name = student.name
            student_dni = student.dni
            action = "entry" if created else "exit"
            time = attendance_record.entry_time if action == "entry" else attendance_record.exit_time
            attendance_status = attendance_record.status
            # Antes de llamar a sendSms, verifica si es la primera vez que se registra la entrada


            if action == "entry" and created:
                # Esto significa que es la primera vez que el estudiante registra su entrada
                # y puedes proceder a enviar el SMS
                sendSms(student_dni, action, time, attendance_status)
            elif action == "exit":
                # Para la salida, siempre envía el SMS, ya que se supone que solo se registra una vez
                sendSms(student_dni, action, time, attendance_status)
            return SuccessResponse(data_=AttendanceRecordDniSerializer(attendance_record).data).send()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def sendSms(student_dni, action, time, status):
    account_sid = 'ACbc58ad6b0a5ac0c5e6964881275e4cbe'
    auth_token = '7d871a7ccd93a41ed5a5bd15994977e5'
    client = Client(account_sid, auth_token)

    try:
        student = Student.objects.get(dni=student_dni)
        parent_phone_number = student.parent.phone_number
    except Student.DoesNotExist:
        print("Estudiante no encontrado")
        return

    local_entry_time = localtime(time, get_default_timezone())
    formatted_time = local_entry_time.strftime('%H:%M')

    # Construir el mensaje basado en la acción
    if action == 'entry':
        body_message = f"\nINFORME DE ASISTENCIA\nNombre: {student.name},\nHora Entrada: {formatted_time},\nEstado: {status}."
    else:  # Para la acción de salida, no incluir el estado
        body_message = f"\nINFORME DE ASISTENCIA\nNombre: {student.name},\nHora Salida: {formatted_time}."
    try:
        message = client.messages.create(
            from_='+16592175883',
            body=body_message,
            to=f'+51{parent_phone_number}'
        )
        print(message.sid)
    except TwilioRestException as e:
        print(f"Error al enviar SMS: {e}")