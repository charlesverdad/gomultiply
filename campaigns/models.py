from django.db import models

# Create your models here.
class Campaign(models.Model):
    cost = models.FloatField(null=True, blank=True)
    location = models.CharField(null=True, max_length=300)
    duration = models.FloatField(null=True, blank=True)
    start_date = models.DateField(null=True)
    difficulty = models.IntegerField(null=True)
    field = models.CharField(null=True, max_length=30)
    requirements = models.CharField(null=True, max_length=200)
    max_people = models.IntegerField(null=True)
    needs = models.CharField(null=True, max_length=200)
    goals = models.CharField(null=True, max_length=200)
