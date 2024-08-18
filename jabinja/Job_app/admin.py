from django.contrib.admin import ModelAdmin, register
from Job_app.models import Job


@register(Job)
class Job_admin(ModelAdmin):
    pass