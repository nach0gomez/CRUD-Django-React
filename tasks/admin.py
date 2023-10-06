from django.contrib import admin
from .models import task

# Register your models here.
# * we add the model to the site page
admin.site.register(task)