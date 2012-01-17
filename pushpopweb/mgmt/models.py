from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DashboardEntry(models.Model):
    checkname = models.CharField(max_length=200, unique=True)

class Dashboard(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    public = models.BooleanField()
    entries = models.ManyToManyField(DashboardEntry)

