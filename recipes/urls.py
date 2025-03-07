from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'), #dessa forma o django vai entender que quando a rota recipes/ vai ser chamada, ele vai chamar a função home
    path('recipes/category/<int:category_id>/', views.category, name='category'), #dessa forma o django vai entender que quando a rota recipes/1 vai ser chamada, ele vai chamar a função recipe
    path('recipes/<int:id>/', views.recipe, name='recipe'), #dessa forma o django vai entender que quando a rota recipes/1 vai ser chamada, ele vai chamar a função recipe
]

#Devemos difinir na configuração da rota o tipo que deve ser aceito na url, nesse caso o tipo inteiro