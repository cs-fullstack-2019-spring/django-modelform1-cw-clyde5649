from django.db import models
from django.utils import timezone


# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=100)
    created_date = models.DateTimeField(max_length=20)
    published_date = models.DateTimeField(max_length=20)