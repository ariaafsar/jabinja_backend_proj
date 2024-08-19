from django.urls import path
from .views import return_jobs, return_job_by_id


urlpatterns = [
    path("", return_jobs),
    path('<str:id_input>/', return_job_by_id)
]