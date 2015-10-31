from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    birthday = models.DateField()
    contact_no = models.CharField(max_length=30)
    password = models.CharField(max_length=30, null=True)
