# Generated by Django 5.0.6 on 2024-06-20 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_doctor_appointment_doctorname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='doctorname',
            new_name='doctor',
        ),
    ]
