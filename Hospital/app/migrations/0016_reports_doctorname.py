# Generated by Django 5.0.6 on 2024-06-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_reports'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='doctorname',
            field=models.CharField(default='Default Doctor', max_length=50),
            preserve_default=False,
        ),
    ]
