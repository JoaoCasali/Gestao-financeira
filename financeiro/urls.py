from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='Login'),
    path('Logout', views.Logout, name='Logout'),
    path('Autenticar', views.Autenticar, name='Autenticar'),

    path('usuario/cadastrar', views.CadastrarUsuario, name='CadastrarUsuário'),
    path('SalvarUsuario/', views.SalvarUsuario, name='SalvarUsuario'),

    path('movimentacoes/listar', views.ListarMovimentacao,
         name='ListarMovimentacao'),
    path('movimentacoes/edicao', views.ChamarTelaCadastrarMovimentacao,
         name='ChamarTelaCadastrarMovimentacao'),
    path('movimentacoes/cadastrar', views.CadastrarMovimentacao,
         name='CadastrarMovimentacao'),
]
