from django.db import models


# Create your models here.

class super_user(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

