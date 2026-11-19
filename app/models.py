from django.db import models

# Create your models here.

class SignUp(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    tech = models.CharField(max_length=15)
    dept = models.CharField(max_length=15)
    shift = models.CharField(max_length=15)
    password = models.CharField(max_length=15)