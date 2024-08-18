from django.db import models


class Job(models.Model):

    category_choises = [
        ("fProgrammer", "Frontend Programmer"), 
        ("bProgrammer", "Backend Programmer"),
    ]

    positon_choises = [
        ("J", "Junior"),
        ("M", "Mid"),
        ("S", "senior"),
    ]

    time_choises = [
        ("ftime", "Full-time"), 
        ("ptime", "Part-time"),
    ]

    salary_choises = [
        ("base", "1000 - 3000 $"),
        ("mid", "3000 - 5000 $"),
        ("top", "5000 - 7000 $"),
    ]

    name = models.CharField(max_length= 100)
    contractor = models.ForeignKey("Contractor_app.Contractor", on_delete= models.CASCADE, null= True)
    location = models.TextField(null= True)
    category = models.CharField(max_length= 100, choices= category_choises)
    position = models.CharField(max_length= 1, choices= positon_choises)
    time_type = models.CharField(max_length=100, choices= time_choises)
    salary = models.CharField(max_length=100, choices= salary_choises)

