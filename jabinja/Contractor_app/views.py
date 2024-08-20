from django.http import HttpResponse, JsonResponse
from .models import Contractor


def return_contractors(request):
    my_dict= Contractor.objects.all().values()
    return JsonResponse(list(my_dict), safe= False)

def return_contractors_by_id(request, id_input):
    contractor = Contractor.objects.get(id = id_input)
    contractor_dict = {
        'id' : contractor.id,
        'name' : contractor.name,
        'location' : contractor.location
    }
    return JsonResponse(contractor_dict, safe= False)

# def return_contractors_by_location(request, location_input):
#     contractors = Contractor.objects.filter(location = location_input)
#     temp = []
#     for item in contractors:
#         temp_dict = {
#             'id' : item.id,
#             'name' : item.name,
#         }
#         temp.append(temp_dict)
#     return JsonResponse(temp, safe= False)

def return_contractors_by_location(request, location_input):
    contractors = Contractor.objects.filter(location = location_input).values('id', 'name')
    return JsonResponse(list(contractors), safe=False)