from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    birthday = models.DateField()
    contact_no = models.CharField(max_length=30)
    #registration_date = models.DateField(_("Date"), datetime.date.today)

 
 #Create tables using
 #python manage.py makemigrations users
 #python manage.py migrate

 #to make account to login to localhost/admin:
 #python manage.py createsuperuser