from django.contrib import admin
from .models import Category, Recipe

# Register your models here.
# aqui as models registradas serão mostrados na área administrativa

class CategoryAdmin(admin.ModelAdmin):
    ...
admin.site.register(Category, CategoryAdmin)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...