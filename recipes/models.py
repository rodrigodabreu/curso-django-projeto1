from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey('Category',
                                  on_delete=models.SET_NULL,
                                    null=True,
                                      blank=True,
                                        default=None #no Python o valor null é None
                                ) #criando o relacionamento de uma model com outra
    author = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )
    # __ (underline underline) é chamado de thunder no Python
    def __str__(self): #função criada para que seja visualizado o nome da categoria no painel de admin de categoria
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=65)
    def __str__(self): #função criada para que seja visualizado o nome da categoria no painel de admin de categoria
        return self.name
    
