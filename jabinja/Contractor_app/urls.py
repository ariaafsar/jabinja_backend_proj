from django.urls import path
from .views import return_contractors, return_contractors_by_id, return_contractors_by_location

urlpatterns = [
    path("", return_contractors),
    path("id/<int:id_input>/", return_contractors_by_id),
    path('location/<str:location_input>/', return_contractors_by_location),
]