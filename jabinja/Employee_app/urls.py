from django.urls import path 
from Employee_app.views import return_user_by_id , return_user_by_phone , return_user_by_email 

urlpatterns = [
    path('id/<str:id_inp>' , return_user_by_id),
    path('phone_number/<str:phone_inp>' , return_user_by_phone),
    path('email/<str:email_inp>' , return_user_by_email),
]

 