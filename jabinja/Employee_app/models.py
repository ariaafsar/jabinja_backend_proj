from django.db import models

class Employee(models.Model) :
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
