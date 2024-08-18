from django.contrib.admin import ModelAdmin, register
from Contractor_app.models import Contractor

@register(Contractor)
class Contractor_admin(ModelAdmin):
    list_display = [
        "name"
    ]

    list_filter = [
        "location"
    ]

    search_fields = [
        "name"
    ]