from django.http import HttpResponse, JsonResponse
from .models import Job


def return_jobs(request):
    jobs_list = Job.objects.all()
    temp = []
    for item in jobs_list:
        jobs_dict = {
            'id' : item.id,
            "name" : item.name,
            'contractor' : item.contractor.name,
            'location' : item.location,
            'category' : item.category,
            'position' : item.position,
            'time type' : item.time_type,
            'salary' : item.salary,
        }
        temp.append(jobs_dict)
    return JsonResponse(temp, safe= False)


def return_job_by_id(request, id_input):
    job = Job.objects.get(id= int(id_input))
    job_dict = {
        "name": job.name,
        "contractor": job.contractor.name,
        "location": job.location,
        "category": job.category,
        "position": job.position,
        "time_type": job.time_type,
        "salary": job.salary,
        }
    return JsonResponse(job_dict)

def return_job_by_location(request, location_input):
    jobs = Job.objects.filter(location= location_input).values('id', 'contractor__name', 'category', 'position', 'time_type', 'salary')
    return JsonResponse(list(jobs), safe=False)
