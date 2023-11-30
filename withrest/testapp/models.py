from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)
#for this employee model we need to define serializer 
#to convert this employee object
#serialaizer are defined in separate file serialisers.py inside our djangoproject directory