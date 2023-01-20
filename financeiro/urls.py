from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='Login'),
    path('usuario/cadastrar', views.cadastrarUsuario, name='Cadastrar usuário'),
]
