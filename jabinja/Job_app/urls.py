from django.urls import path
from .views import return_jobs, return_job_by_id, return_job_by_location


urlpatterns = [
    path("", return_jobs),
    path('id/<str:id_input>/', return_job_by_id),
    path('location/<str:location_input>', return_job_by_location)

]