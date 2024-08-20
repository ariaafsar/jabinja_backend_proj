from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job/', include('Job_app.urls')),
    path("contractor/", include('Contractor_app.urls')),
    path('employee/' , include('Elmployee_app.urls')),
]
