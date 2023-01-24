from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Usuario, Movimentacao


def listarMovimentacoes(request):
    return render(request, 'movimentacoes/listar.html')


def login(request):
    return render(request, 'usuario/login.html')


def cadastrarUsuario(request):
    return render(request, 'usuario/cadastrar.html')
    
def movimentacao(request):
    movimentacoes = Movimentacao.objects.all().order_by('data_movimentacao')
    conteudo = {
        'movimentacoes': movimentacoes
    }
    return render(request,'movimentacoes/listar.html', conteudo)

def cadastrarMovimentacao(request):
    usuario = request.POST['usuario']
    data_movimentacao = request.POST['data_movimentacao']
    valor = request.POST['valor']
    descricao = request.POST['descricao']
    Movimentacao.objects.create(usuario=usuario,data_movimentacao=data_movimentacao,valor=valor,descricao=descricao)
    return render(request, 'movimentacoes/cadastrar.html')