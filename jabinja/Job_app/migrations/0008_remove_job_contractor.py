# Generated by Django 5.1 on 2024-08-18 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Job_app', '0007_job_contractor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='contractor',
        ),
    ]
