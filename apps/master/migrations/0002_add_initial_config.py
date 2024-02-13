# Generated by Django XXX on YYYY-MM-DD HH:MM
from django.db import migrations
from django.conf import settings

UserName = 'admin'
def create_superuser(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)

    if not User.objects.filter(username=UserName).exists():
        User.objects.create_superuser(UserName, 'correo@example.com', '12345')

def add_initial_system_users(apps, schema_editor):
    SystemUser = apps.get_model('master', 'SystemUser')
    User = apps.get_model('auth', 'User')

    auth_user, created = User.objects.get_or_create(
        username=UserName,
        defaults={
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'email@example.com'
        }
    )
    if created:
        auth_user.set_password('contraseña_segura')
        auth_user.save()

    # Ahora, crea el SystemUser asociado
    SystemUser.objects.create(
        status='ACTIVE',
        auth_user=auth_user,
        document_type='DNI',
        document='12345678',
        gender='Masculino',
        phone='123456789',
        entity='Entidad X',
        avatar='url/avatar.jpg'
    )

def add_initial_systems(apps, schema_editor):
    System = apps.get_model('master', 'System')
    System.objects.create(
        name="Academia",
        description="Descripción del Sistema",
        icon="icon",
        color="color",
        version="1.0",
        order=1,
        url=""
)

def add_initial_profile(apps, schem_editor):
    # Obtener el modelo Profile
    Profile = apps.get_model('master', 'Profile')

    # Añadir un registro inicial con el nuevo campo ProfileStatus
    Profile.objects.create(
        name=UserName,
        description="Descripción del Perfil",
        domain="Dominio",
        type="Tipo",
        icon="icono",
    )

def add_initial_user_profile(apps, schem_editor):
    SystemUserProfile = apps.get_model('master', 'SystemUserProfile')
    SystemUser = apps.get_model('master', 'SystemUser')
    Profile = apps.get_model('master', 'Profile')

    system_user = SystemUser.objects.first()
    profile = Profile.objects.first()


    SystemUserProfile.objects.create(
        system_user=system_user,
        profile=profile,
    )

def add_initial_modules(apps, schem_editor):
    Module = apps.get_model('master', 'Module')
    System = apps.get_model('master', 'System')

    system = System.objects.first()

    Module.objects.create(
        system=system,
        name="Turnos",
        description="Turnos como mañana, tarde ",
        version="1.0",
        url="/shift",
        order=1,
        icon="cilClock",
    )

    Module.objects.create(
        system=system,
        name="Asistencia",
        description="Gestión de asistencia",
        version="1.0",
        url="/attendance",
        order=4,
        icon="cilClipboard",
    )

    Module.objects.create(
        system=system,
        name="Padres",
        description="Gestión de padres",
        version="1.0",
        url="/parent",
        order=2,
        icon="cilClipboard",
    )

    Module.objects.create(
        system=system,
        name="Estudiantes",
        description="Gestión de estudiantes",
        version="1.0",
        url="/student",
        order=3,
        icon="cilClipboard",
    )

def add_initial_access(apps, schem_editor):
    Access = apps.get_model('master', 'Access')
    Module = apps.get_model('master', 'Module')
    Profile = apps.get_model('master', 'Profile')

    module_attendance = Module.objects.get(name="Asistencia")
    module_shift = Module.objects.get(name="Turnos")
    module_parent = Module.objects.get(name="Padres")
    module_student = Module.objects.get(name="Estudiantes")
    profile = Profile.objects.first()

    Access.objects.create(
        module=module_attendance,
        profile=profile
    )

    Access.objects.create(
        module=module_shift,
        profile=profile
    )

    Access.objects.create(
        module=module_parent,
        profile=profile
    )

    Access.objects.create(
        module=module_student,
        profile=profile
    )


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
        migrations.RunPython(add_initial_system_users),
        migrations.RunPython(add_initial_systems),
        migrations.RunPython(add_initial_profile),
        migrations.RunPython(add_initial_user_profile),
        migrations.RunPython(add_initial_modules),
        migrations.RunPython(add_initial_access),
    ]