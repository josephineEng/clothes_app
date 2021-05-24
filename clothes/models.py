from django.db import models

# Create your models here.

class Gender(models.Model):
    Male   = "M"
    Female = "F"
    gender =[(
    Male,"M"
    ),(Female,"F")]



    genderSelection=models.CharField(max_length=1,
    choices=gender,default="F")

