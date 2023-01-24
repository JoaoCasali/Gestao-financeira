from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='Login'),
    path('usuario/cadastrar', views.CadastrarUsuario, name='CadastrarUsuário'),
    path('SalvarUsuario/', views.SalvarUsuario, name='SalvarUsuario'),
    path('movimentacao/listar', views.ListarMovimentacao,
         name='ListarMovimentacao'),
]
