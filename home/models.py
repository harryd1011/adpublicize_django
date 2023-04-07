from django.db import models

# Create your models here.

class User(models.Model):
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    email = models.EmailField()
    password= models.CharField(max_length=255)
    resi_add= models.CharField(max_length=150)
    office_add= models.CharField(max_length=150)
    office_contact= models.CharField(max_length=20)
    area= models.CharField(max_length=20)
    pincode= models.CharField(max_length=10)
