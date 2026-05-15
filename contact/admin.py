from django.contrib import admin
from contact import models #from contact import models / (models.Contact)

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','name','aka','email',
    ordering = '-id',
    search_fields = 'id','name','aka','email',
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = 'name',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'names',
    ordering = '-id',