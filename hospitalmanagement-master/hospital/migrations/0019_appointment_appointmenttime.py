# Generated by Django 3.0.5 on 2024-05-30 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointmentTime',
            field=models.TimeField(auto_now=True),
        ),
    ]
