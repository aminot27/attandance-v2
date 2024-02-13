# Generated by Django 4.0 on 2024-02-12 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('UPDATED', 'UPDATED'), ('DELETED', 'DELETED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('academy_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('name2', models.CharField(max_length=255, verbose_name='Name')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Academy',
                'verbose_name_plural': 'Academies',
                'db_table': 'academy_academy',
                'ordering': ['academy_id'],
            },
        ),
        migrations.CreateModel(
            name='HikCentralAccessRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('UPDATED', 'UPDATED'), ('DELETED', 'DELETED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('employee_id', models.CharField(max_length=255, verbose_name='Employee ID')),
                ('access_date_time', models.DateTimeField(verbose_name='Access Date and Time')),
                ('access_date', models.DateField(verbose_name='Access Date')),
                ('access_time', models.TimeField(verbose_name='Access Time')),
            ],
            options={
                'verbose_name': 'HikCentral Access Record',
                'verbose_name_plural': 'HikCentral Access Records',
                'db_table': 'hikcentral_access_record',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('UPDATED', 'UPDATED'), ('DELETED', 'DELETED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('parent_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Parent',
                'verbose_name_plural': 'Parents',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('UPDATED', 'UPDATED'), ('DELETED', 'DELETED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('shift_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('entry_start', models.TimeField(blank=True, null=True, verbose_name='Inicio Temprano')),
                ('entry_end', models.TimeField(blank=True, null=True, verbose_name='Fin Temprano')),
                ('early_until', models.TimeField(blank=True, null=True, verbose_name='Early until')),
                ('late_until', models.TimeField(blank=True, null=True, verbose_name='Late until')),
                ('leave_start', models.TimeField(blank=True, null=True, verbose_name='Inicio Salida')),
                ('leave_end', models.TimeField(blank=True, null=True, verbose_name='Fin Salida')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeeklyShift',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('UPDATED', 'UPDATED'), ('DELETED', 'DELETED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('weekly_shift_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Weekly shift')),
                ('friday_shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_shifts', to='warehouse.shift')),
                ('monday_shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_shifts', to='warehouse.shift')),
                ('saturday_shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_shifts', to='warehouse.shift')),
                ('sunday_shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_shifts', to='warehouse.shift')),
                ('thursday_shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_shifts', to='warehouse.shift')),
                ('tuesday_shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_shifts', to='warehouse.shift')),
                ('wednesday_shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_shifts', to='warehouse.shift')),
            ],
            options={
                'verbose_name': 'Weekly Shift',
                'verbose_name_plural': 'Weekly Shifts',
                'db_table': 'weekly_shifts',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('UPDATED', 'UPDATED'), ('DELETED', 'DELETED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('student_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.ForeignKey(db_column='parent_id', on_delete=django.db.models.deletion.DO_NOTHING, to='warehouse.parent', verbose_name='Parent')),
                ('shift', models.ForeignKey(db_column='shift_id', on_delete=django.db.models.deletion.DO_NOTHING, to='warehouse.shift', verbose_name='Shift')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationRecord',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('UPDATED', 'UPDATED'), ('DELETED', 'DELETED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('location_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='Timestamp')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Latitude')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Longitude')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.student', verbose_name='Student')),
            ],
            options={
                'verbose_name': 'Location Record',
                'verbose_name_plural': 'Location Records',
                'db_table': 'academy_location_record',
                'ordering': ['location_id'],
            },
        ),
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('attendance_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField(auto_now_add=True, verbose_name='Hora de Entrada')),
                ('exit_time', models.DateTimeField(blank=True, null=True, verbose_name='Hora de Salida')),
                ('status', models.CharField(choices=[('Early', 'Temprano'), ('Late', 'Tarde'), ('Absent', 'Ausente')], default='Absent', max_length=12, verbose_name='Estado de Asistencia')),
                ('entry_sms_sent', models.BooleanField(default=False)),
                ('exit_sms_sent', models.BooleanField(default=False)),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.shift', verbose_name='Turno')),
                ('student', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.DO_NOTHING, to='warehouse.student', verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Registro de Asistencia',
                'verbose_name_plural': 'Registros de Asistencia',
                'db_table': 'academy_attendance_record',
                'ordering': ['attendance_id'],
            },
        ),
    ]
