"""master_serv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from master_serv.views.authentication_view import AuthenticationView

schema_view = get_schema_view(
    openapi.Info(title="MASTER-API",
                 default_version='BASE DEV TEMPLATE API',
                 description="",
                 terms_of_service="https://www.google.com/policies/terms/",
                 contact=openapi.Contact(email="josecarloshq@gmail.com"),
                 license=openapi.License(name="BSD License"),
                 ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                  path('api/authentication/', AuthenticationView.as_view(), name='create_token'),
                  # path('api/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh_token'),
                  path('api/master/', include('apps.master.urls')),
                  re_path('api/warehouse/', include('apps.warehouse.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
