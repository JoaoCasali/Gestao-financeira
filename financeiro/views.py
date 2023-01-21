from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Usuario, Movimentacao


def listarMovimentacoes(request):
    return render(request, 'movimentacoes/listar.html')


def login(request):
    return render(request, 'usuario/login.html')


def cadastrarUsuario(request):
    return render(request, 'usuario/cadastrar.html')

def movimentacao(request):
    movimentacoes = Movimentacao.objects.all()
    conteudo = {
        'movimentacoes': movimentacoes
    }
    return render(request,'movimentacoes/listar.html', conteudo)