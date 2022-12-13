from django.db import models
from Adminapp.models import *
import datetime



# Create your models here.
class Contactdb(models.Model):
    message = models.TextField(max_length=30)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    subject = models.TextField(max_length=30)

class Registrationdb(models.Model):
    firstname = models.CharField(max_length=20,default='')
    lastname = models.CharField(max_length=20,default='')
    phone = models.IntegerField()
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Cartdb(models.Model):
    serviceid = models.ForeignKey(Serverdb, on_delete=models.CASCADE)
    userid = models.ForeignKey(Registrationdb, on_delete=models.CASCADE)
    total = models.IntegerField()
    status = models.IntegerField(default = 0)

class Bookingdb(models.Model):
    userid = models.ForeignKey(Registrationdb, on_delete=models.CASCADE)
    cartid = models.ForeignKey(Cartdb, on_delete=models.CASCADE)
    date = models.DateField(default = '2020-02-03')
    time = models.TimeField(default = '08:10:10')
    





    

