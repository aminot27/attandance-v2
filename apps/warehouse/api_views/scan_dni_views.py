from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from django.utils.timezone import localtime
from rest_framework.response import Response
from apps.warehouse.models.student_model import Student
from apps.warehouse.models.shift_model import Shift
from apps.warehouse.models.attendance_record_model import AttendanceRecord
from apps.warehouse.serializers.scan_dni_serializers import ScanDniRequestSerializer, AttendanceRecordDniSerializer
from master_serv.utils.success_response import SuccessResponse
from rest_framework.exceptions import NotFound, ValidationError

class ScanDniView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ScanDniRequestSerializer, responses={status.HTTP_200_OK: AttendanceRecordDniSerializer()})
    def post(self, request):
        serializer = ScanDniRequestSerializer(data=request.data)
        if serializer.is_valid():
            dni = serializer.validated_data['dni']
            try:
                student = Student.objects.get(dni=dni)
            except Student.DoesNotExist:
                raise NotFound(detail="Estudiante no encontrado")

            now = localtime()
            shifts = Shift.objects.filter(start_time__lte=now, end_time__gte=now)
            shift = shifts.first()
            if not shift:
                raise ValidationError({'error': 'No hay turnos activos en este momento'})

            attendance_record = AttendanceRecord(student=student, shift=shift)
            attendance_record.save()

            return SuccessResponse(data_=AttendanceRecordDniSerializer(attendance_record).data).send()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)