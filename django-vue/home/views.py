import re, csv, io
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import Usuario_Cadastro,  Login
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from passlib.hash import pbkdf2_sha256
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from .models import Usuarios, AuthUser
from django.contrib import messages
from django.urls import reverse



from .models import Empresas

#PAGINA INICIAL
def first(request):
    return render(request, 'home/index.html')


def do_login(request):

    formularioLogin = Login(request.POST or None)
    
    if request.method == 'POST':

        if formularioLogin.is_valid():
            
                username = formularioLogin.cleaned_data['username']
                password = formularioLogin.cleaned_data['senha']
                
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('/INDEX')
                    
                else:
                    return render(request, 'home/index.html')
        else:
            return render(request, 'home/login.html', {'formLogin': formularioLogin})
    else:
        return render(request, 'home/login.html', {'formLogin': formularioLogin})



def cadastre(request):
    
    form = Usuarios(request.POST or None)

    if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['nome']
        email = request.POST['email']
        password = request.POST['senha']
        

        hasher = PBKDF2PasswordHasher()

        enc_password = hasher.encode(password=password,
                                  salt='salt',
                                  iterations=50000)
        

                
        Usuarios.objects.create(
            username = username,
            nome = first_name,            
            email = email,
            senha = enc_password 
            ) 

        messages.add_message(request, messages.SUCCESS, 'Usuario cadastrado com sucesso ')
        return render(request, 'home/cadastro.html', {'form': form  })
        
    else:
        
        return render(request, 'home/cadastro.html', {'form': form})


@login_required
class EmpresasList(ListView):
    model = Empresas

@login_required
def index(request):
    Emp = Empresas.objects.all()
    
    context = {
        'Empresas': Emp,
    }

    return render(request,'home/empresas_list.html', context)


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

def validarEmails(request):
    return render(request, 'home/validarEmails.html')    



@login_required
def arquivos(request):
    template = "home/validarEmails.html"

    if request.method == 'GET':
        return render(request,template)

    try:
        csv_file = request.FILES['file']
        
        if not csv_file.name.endswith('.csv'):
            messages.add_message(request, messages.error, 'Arquivo não é csv ')

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)


        

        email = csv.reader(io_string, delimiter=',', quotechar="|")
        
        return render(request, template, {'email': email})
    
    except:
        messages.add_message(request, messages.INFO, 'ARQUIVO NÃO CARREGADO')
        return render(request, template)


@login_required
def painel(request):
    template = "home/painel.html"

    return render(request, template)

