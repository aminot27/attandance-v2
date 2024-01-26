from django.urls import path

from apps.master.api_views.authorization_views import AuthorizationView
from apps.master.api_views.lov_views import LovsView, LovView, LovDetailView
from apps.master.api_views.system_user_views import SystemUserRegister, ResetPassword, ChangePassword, SystemUsersView, \
    SystemUserView

urlpatterns = [
    path('authorization/', AuthorizationView.as_view(), name='filer_system_users'),
    path('system_user/filters/', SystemUsersView.as_view(), name='filer_system_users'),
    # path('system_user/register/', SystemUserRegister.as_view(), name='user_register'),
    path('system_user/create/', SystemUserView.as_view(), name='user_create'),
    path('system_user/reset_password/', ResetPassword.as_view(), name='reset_password'),
    path('system_user/change_password/', ChangePassword.as_view(), name='change_password'),
    path('lov/', LovView.as_view(), name='create_lov'),
    path('lov/<int:pk>/', LovDetailView.as_view(), name='lov_detail'),
    path('lov/filter/', LovsView.as_view(), name='filter_lovs'),
]
