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
                defaults={'status': 'Absent'}  # Inicializa con 'Absent'
            )

            # Verifica si el escaneo ocurre dentro del intervalo de salida
            if current_shift.leave_start <= now_time <= current_shift.leave_end:
                # Solo actualiza exit_time si el registro ya existe y el estudiante ya marcó entrada
                if not created and attendance_record.entry_time:
                    attendance_record.exit_time = localtime(now())
                    attendance_record.save()

            # Actualiza el estado si el registro es nuevo o el estudiante estaba marcado como ausente
            if created or attendance_record.status == 'Absent':
                if current_shift.early_start <= now_time <= current_shift.early_end:
                    attendance_record.status = 'Absent'
                elif current_shift.late_start <= now_time <= current_shift.late_end:
                    attendance_record.status = 'Late'
                attendance_record.save()

            return SuccessResponse(data_=AttendanceRecordDniSerializer(attendance_record).data).send()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)