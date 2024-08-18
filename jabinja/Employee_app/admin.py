from django.contrib.admin import register , ModelAdmin
from Employee_app.models import Employee

@register(Employee)
class Employee_Admin(ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone_number',
    ]
    search_fields = [
        'name',
        'phone_number',
    ]
# Register your models here.
