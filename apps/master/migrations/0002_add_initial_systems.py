# Generated by Django 4.0 on 2024-01-27 06:08
from django.db import migrations
def add_initial_systems(apps, schema_editor):
    System = apps.get_model('master', 'System')
    System.objects.create(
        name="john",
        description="Descripción del Sistema",
        icon="",
        color="",
        version="1.0",
        order=1,
        url=""
)
class Migration(migrations.Migration):
    dependencies = [
        ('master', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_initial_systems),
    ]
