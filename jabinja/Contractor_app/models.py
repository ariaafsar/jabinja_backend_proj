from django.db import models


class Contractor(models.Model):
    name = models.CharField(max_length= 100, null= True)
    location = models.TextField(null= True)
    
    def __str__(self) -> str:
        return self.name