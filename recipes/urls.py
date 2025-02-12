from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe), #dessa forma o django vai entender que quando a rota recipes/1 vai ser chamada, ele vai chamar a função recipe
]

#Devemos difinir na configuração da rota o tipo que deve ser aceito na url, nesse caso o tipo inteiro