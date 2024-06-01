# Generated by Django 3.0.5 on 2024-05-30 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_appointment_appointmenttime'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40)),
                ('assignedDoctorName', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('symptoms', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
