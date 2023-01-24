from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Usuario, Movimentacao

from django.views.decorators.csrf import csrf_protect


def Login(request):
    return render(request, 'usuario/login.html')


def CadastrarUsuario(request):
    return render(request, 'usuario/edicao.html')


def SalvarUsuario(request):
    nome = request.POST.get('usuario')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuario()

    usuario.nome = nome
    usuario.senha = senha
    usuario.email = email

    usuario.save()

    request.session['idUsuario'] = usuario.id

    return redirect("ListarMovimentacao")


def ListarMovimentacao(request):
    movimentacoes = Movimentacao.objects.all()
    conteudo = {
        'movimentacoes': movimentacoes
    }
    return render(request, 'movimentacoes/listar.html', conteudo)
