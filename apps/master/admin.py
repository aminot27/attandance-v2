# Register your models here.
from django.contrib import admin

from apps.master.models.access_model import Access
from apps.master.models.lov_model import Lov
from apps.master.models.module_model import Module
from apps.master.models.movement_model import Movement
from apps.master.models.profile_model import Profile
from apps.master.models.system_model import System
from apps.master.models.system_user_model import SystemUser
from apps.master.models.system_user_profile_model import SystemUserProfile


@admin.register(SystemUser)
class SystemUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SystemUser._meta.fields]


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Access._meta.fields]


@admin.register(Lov)
class LovAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Lov._meta.fields]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Module._meta.fields]


@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Movement._meta.fields]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in System._meta.fields]


@admin.register(SystemUserProfile)
class SystemUserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SystemUserProfile._meta.fields]
