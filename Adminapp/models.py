from django.db import models

# Create your models here.
class Branchdb(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=30)
    image = models.ImageField(upload_to = 'Image',default = "null.jpg")

class Serverdb(models.Model):
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'Image',default = "null.jpg")