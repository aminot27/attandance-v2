# Generated by Django 4.0 on 2024-01-27 06:08
from django.db import migrations
def add_initial_system_users(apps, schema_editor):
    SystemUser = apps.get_model('master', 'SystemUser')
    User = apps.get_model('auth', 'User')

    # Primero, crea o obtén el usuario de autenticación
    auth_user, created = User.objects.get_or_create(
        username='john',
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
        auth_user=auth_user,
        document_type='DNI',
        document='12345678',
        gender='Masculino',
        phone='123456789',
        entity='Entidad X',
        avatar='url/avatar.jpg'
    )
class Migration(migrations.Migration):
    dependencies = [
        ('master', '0002_add_initial_systems'),
    ]
    operations = [
        migrations.RunPython(add_initial_system_users),
    ]
