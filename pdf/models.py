from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    summary = models.TextField(max_length=1000)
    degree = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    work_experience = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)