from django.http.response import JsonResponse , HttpResponse
from Employee_app.models import Employee
from django.forms.models import model_to_dict


def return_employees(request):
    employee_lst = Employee.objects.all()
    lst = []
    for i in employee_lst :
        employee_lst = {
            'id' : i.id,
            'name' : i.name,
            'email' : i.email,
            'phone_number' : i.phone_number,
        }
        lst.append(employee_lst)
    return JsonResponse(lst , safe= False)


def return_user_by_id(request , id_inp) :
    employee = Employee.objects.get(id= int(id_inp))
    return JsonResponse(model_to_dict(employee), safe= False)

