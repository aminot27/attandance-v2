from django.utils.timezone import localtime, now
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
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

            attendance_record, created = AttendanceRecord.objects.get_or_create(
                student=student,
                shift=current_shift,
                defaults={'status': 'Falta'}  # Inicializa con 'Absent'
            )

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
            sendSms(student_dni, action, time, attendance_status)
            return SuccessResponse(data_=AttendanceRecordDniSerializer(attendance_record).data).send()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def sendSms(student_dni, action, time, status):
    account_sid = 'ACbc58ad6b0a5ac0c5e6964881275e4cbe'
    auth_token = '4759a8f614c076955f56eed09fad331a'
    client = Client(account_sid, auth_token)

    try:
        student = Student.objects.get(dni=student_dni)
        parent_phone_number = student.parent.phone_number
    except Student.DoesNotExist:
        print("Estudiante no encontrado")
        return

    local_entry_time = localtime(time, get_default_timezone())
    formatted_time = local_entry_time.strftime('%H:%M')

    body_message = f"\nINFORME DE ASISTENCIA\nNombre: {student.name},\nHora {('Entrada' if action == 'entry' else 'Salida')}: {formatted_time},\nEstado: {status}."

    message = client.messages.create(
        from_='+16592175883',
        body=body_message,
        to=f'+51{parent_phone_number}'
    )

    print(message.sid)