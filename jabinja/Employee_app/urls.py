from django.urls import path 
from Employee_app.views import return_user_by_id , return_employees

urlpatterns = [
    path('', return_employees),
    path('id/<str:id_inp>' , return_user_by_id)
    ]