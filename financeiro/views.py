from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from .models import Usuario, Movimentacao


def Login(request):
    return render(request, 'usuario/login.html')


def CadastrarUsuario(request):
    return render(request, 'usuario/edicao.html')


def Autenticar(request):
    nome = request.POST.get('usuario')
    senha = request.POST.get('senha')

    try:
        usuario = Usuario.objects.get(nome=nome)

    except:
        messages.warning(request, 'Usuário não encontrado')
        return redirect('Login')

    if usuario.senha == senha:
        request.session['idUsuario'] = usuario.id
        return redirect('ListarMovimentacao')

    messages.warning(request, 'Senha incorreta')
    return redirect('Login')


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
    idUsuario = request.session['idUsuario']
    if idUsuario <= 0:
        messages.warning(request, 'Sua sessão expirou!')
        return redirect('Login')

    try:
        usuario = Usuario.objects.get(pk=idUsuario)

    except:
        messages.warning(request, 'Usuário não encontrado')
        return redirect('Login')

    movimentacoes = Movimentacao.objects.all().filter(usuario=usuario)
    conteudo = {
        'movimentacoes': movimentacoes
    }
    return render(request, 'movimentacoes/listar.html', conteudo)


def ChamarTelaCadastrarMovimentacao(request):
    idUsuario = request.session['idUsuario']
    if idUsuario <= 0:
        messages.warning(request, 'Sua sessão expirou!')
        return redirect('Login')

    return render(request, 'movimentacoes/edicao.html')


def CadastrarMovimentacao(request):
    idUsuario = request.session['idUsuario']
    if idUsuario <= 0:
        messages.warning(request, 'Sua sessão expirou!')
        return redirect('Login')

    try:
        usuario = Usuario.objects.get(pk=idUsuario)

    except:
        messages.warning(request, 'Usuário não encontrado')
        return redirect('Login')

    data_movimentacao = request.POST.get('data_movimentacao')
    valor = request.POST.get('valor')
    descricao = request.POST.get('descricao')

    movimentacao = Movimentacao()
    movimentacao.usuario = usuario
    movimentacao.data_movimentacao = data_movimentacao
    movimentacao.valor = valor
    movimentacao.descricao = descricao
    movimentacao.save()

    return redirect("ListarMovimentacao")


def Logout(request):
    request.session['idUsuario'] = 0

    return redirect("Login")
