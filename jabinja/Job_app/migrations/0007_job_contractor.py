# Generated by Django 5.1 on 2024-08-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_app', '0006_alter_job_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='contractor',
            field=models.CharField(default='digi kala', max_length=100),
            preserve_default=False,
        ),
    ]
