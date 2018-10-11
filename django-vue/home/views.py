import re
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import Usuario_Cadastro,  Login

from django.contrib.auth.models import User
from django.contrib import messages
from passlib.hash import pbkdf2_sha256
from .models import Usuarios, AuthUser


from .models import Empresas

#PAGINA INICIAL
def first(request):
    return render(request, 'home/index.html')


def do_login(request):

    form = Login(request.POST or None)

    if request.method == 'POST' and form.is_valid():
                
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home/empresas_list.html')
            
        else:
            return render(request, 'home/index.html')
    else:
        return render(request, 'home/login.html', {'formularioLogin': form})



def cadastre(request):
    
    form = Usuario_Cadastro(request.POST or None)

    if form.is_valid():

        username = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']


        enc_password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)

        AuthUser.objects.create(
            username = username,
            first_name = first_name,
            email = email,
            password = enc_password
            
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


#Funcao para logout
def do_logout(request):
    logout(request)
    return render(request, 'home/index.html')
