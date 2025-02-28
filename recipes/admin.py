from django.contrib import admin
from .models import Category

# Register your models here.
# aqui as models registradas serão mostrados na área administrativa

class CategoryAdmin(admin.ModelAdmin):
    ...
admin.site.register(Category, CategoryAdmin)