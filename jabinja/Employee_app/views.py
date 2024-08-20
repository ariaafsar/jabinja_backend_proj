from django.http.response import JsonResponse , HttpResponse
from Employee_app.models import Employee
def return_employees(request):
    employee_lst = Employee.objects.all()
    lst = []
    for i in employee_lst :
        employee_lst = {
            'name' : i.name,
            'email' : i.email,
            'phone_number' : i.email,
        }
        lst.append(employee_lst)
    return JsonResponse(lst , safe= False)

def return_user_by_id(request , id_inp) :
    employee = Employee.objects.get(id_inp)
def return_user_by_phone(request , phone_inp):
    pass
def return_user_by_email(request , email_inp):
    pass
# Create your views here.
