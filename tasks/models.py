from django.db import models

# Create your models here.

# * heritance from models
class task(models.Model):
    # * a title for each task
    title = models.CharField(max_length=200)
    # * description for each task
    description = models.TextField(blank=True) #* can be blank
    # * verify if it is done or not
    done = models.BooleanField(default=False) #* default is false
    