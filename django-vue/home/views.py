import re
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import Usuario_Cadastro
from django.contrib.auth.models import User
from django.contrib import messages
from passlib.hash import pbkdf2_sha256
from .models import Usuarios


from .models import Empresas

#PAGINA INICIAL
def first(request):
    return render(request, 'home/index.html')


#Funcao para logout
def do_logout(request):
    logout(request)
    return render(request, 'home/index.html')

def cadastre(request):
    
    form = Usuario_Cadastro(request.POST or None)

    if form.is_valid():

        username = request.POST['username']
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['senha']


        enc_password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)

        Usuarios.objects.create(
            username = username,
            nome = nome,
            email = email,
            senha = enc_password
            
        ) 

        messages.success(request, 'Cadastro efetuado com sucesso')     
        return render(request, 'home/cadastro.html', {'form': form })
    else:
        
        return render(request, 'home/cadastro.html', {'form': form})


@login_required
class EmpresasList(ListView):
    model = Empresas

@login_required
def index(request):
    Emp = Empresas.objects.all()
    return render(request,'home/empresas_list.html',{'Empresas': Emp })


@login_required
def pesquisar(request):
    pesquisa = request.GET.get('searchCNPJ', None)
    if pesquisa:
        pesquisa = re.sub(r"\D", "", pesquisa)        
        emp = Empresas.objects.filter(doc=pesquisa)   
        return render(request, '/empresas_detail.html', {'Empresas': emp})
    else:
       return redirect('index')


#Funcão para mostrar os detalhes do CNPJ
class listarCnpjView(DetailView):
    model = Empresas
    template_name='home/empresas_detail.html'
    context_object_name = 'emp_detail'

