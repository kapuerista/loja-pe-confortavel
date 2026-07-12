from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path(
        'clientes/cadastrar/',
        views.cadastrar_cliente,
        name='cadastrar_cliente'
    ),

    path(
        'clientes/',
        views.lista_clientes,
        name='lista_clientes'
    ),

    path(
    'clientes/editar/<int:id>/',
    views.editar_cliente,
    name='editar_cliente'
    ),
    
    path(
        'produtos/cadastrar/',
        views.cadastrar_produto,
        name='cadastrar_produto'
    ),

    path(
        'produtos/',
        views.lista_produtos,
        name='lista_produtos'
    ),

    path(
    'produtos/editar/<int:id>/',
    views.editar_produto,
    name='editar_produto'
    ),

    path(
        'fabricantes/',
        views.fabricante_construcao,
        name='fabricantes'
    ),

    path(
    'produtos/excluir/<int:id>/',
    views.excluir_produto,
    name='excluir_produto'
    ),
]