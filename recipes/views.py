from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe
from .models import Recipe
from django.http import Http404

#get_list_or_404 -> retorna uma lista de objetos ou retorna um erro 404 caso não encontre
#get_object_or_404 -> retorna um objeto ou retorna um erro 404 caso não encontre

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, "recipes/pages/home.html", context={
        'recipes': recipes,
    })
def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id #filtra os objetos da categoria que tem o id igual ao id passado na url
    #     , is_published=True
    # ).order_by('-id')

    # if not recipes:
    #     raise Http404(f'Category with id {category_id} not found 🫤')
    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id #filtra os objetos da categoria que tem o id igual ao id passado na url
        , is_published=True
    ).order_by('-id'),
     category__id=category_id, is_published=True)
            
    return render(request, "recipes/pages/category.html", context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |' 
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published = True)

    return render(request, "recipes/pages/recipe-view.html", context={
        'recipe':recipe,
        'is_detail_page': True,
})