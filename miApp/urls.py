from django.urls import path
from miApp.views import mostrar_familia, mostrar_amigos, mostrar_compañeros, mostrar_inicio


urlpatterns = [
    path('/familia',mostrar_familia, name='familia'),
    path('/amigos',mostrar_amigos, name='amigos' ),
    path('/compañeros',mostrar_compañeros, name='compañeros'),
    path('', mostrar_inicio, name='inicio'),
]
