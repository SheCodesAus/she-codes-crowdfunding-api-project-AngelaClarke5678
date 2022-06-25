from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.CharField(max_length=200)