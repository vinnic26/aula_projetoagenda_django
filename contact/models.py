from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    names = models.CharField(max_length=50)
    def __str__(self):
        return self.names

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True)
    aka = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.name}'