from django.contrib.admin import ModelAdmin, register
from Job_app.models import Job


@register(Job)
class Job_admin(ModelAdmin):
    list_display = [
        "name",
        "position",
        "category",
    ]

    list_filter = [
        "location"
    ]