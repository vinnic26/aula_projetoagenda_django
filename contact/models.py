from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True)
    aka = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)