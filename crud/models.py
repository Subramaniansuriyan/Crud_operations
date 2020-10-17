from django.db import models

# Create your models here.

class Member(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phonenumber=models.IntegerField()
    email=models.EmailField(max_length=255)
    role=models.BooleanField(default=False)