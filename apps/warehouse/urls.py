from django.urls import path

from apps.warehouse.api_views.academy_views import AcademyView, AcademiesView, AcademyDetailView
from apps.warehouse.api_views.attendace_record_views import AttendanceRecordView, AttendanceRecordsView, \
    AttendanceRecordDetailView
from apps.warehouse.api_views.location_record_views import LocationRecordView, LocationRecordsView, \
    LocationRecordDetailView
from apps.warehouse.api_views.parent_views import ParentView, ParentsView, ParentDetailView
from apps.warehouse.api_views.scan_dni_views import ScanDniView
from apps.warehouse.api_views.shift_views import ShiftView, ShiftsView, ShiftDetailView
from apps.warehouse.api_views.student_views import (
    StudentView,
    StudentsView,
    StudentDetailView
)

urlpatterns = [
    path('student/', StudentView.as_view(), name='create_student'),
    path('students/filter/', StudentsView.as_view(), name='filter_students'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='modify_student'),

    path('academy/', AcademyView.as_view(), name='create_academy'),
    path('academies/filter/', AcademiesView.as_view(), name='filter_academies'),
    path('academy/<int:pk>/', AcademyDetailView.as_view(), name='modify_academy'),


    path('attendance_record/', AttendanceRecordView.as_view(), name='create_attendance_record'),
    path('attendance_records/filter/', AttendanceRecordsView.as_view(), name='filter_attendance_records'),
    path('attendance_record/<int:pk>/', AttendanceRecordDetailView.as_view(), name='modify_attendance_record'),

    path('location_record/', LocationRecordView.as_view(), name='create_location_record'),
    path('location_records/filter/', LocationRecordsView.as_view(), name='filter_location_records'),
    path('location_record/<int:pk>/', LocationRecordDetailView.as_view(), name='modify_location_record'),

    path('parent/', ParentView.as_view(), name='create_parent'),
    path('parents/filter/', ParentsView.as_view(), name='filter_parents'),
    path('parent/<int:pk>/', ParentDetailView.as_view(), name='modify_parent'),

    path('shift/', ShiftView.as_view(), name='create_shift'),
    path('shifts/filter/', ShiftsView.as_view(), name='filter_shifts'),
    path('shift/<int:pk>/', ShiftDetailView.as_view(), name='modify_shift'),

    path('scan/', ScanDniView.as_view(), name='scan_attendance'),
]

#hi