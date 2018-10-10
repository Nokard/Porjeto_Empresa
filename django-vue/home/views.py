import re
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import Usuario_Cadastro


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

    if request.method == 'POST':
        form = Usuario_Cadastro(request.POST)
        
        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data
            #username = form.cleaned_data["username"]
            #password = form.cleaned_data["senha"]

            #user.set_password(password)
            user.save()    
            msg = 'cadastrado com sucesso'        
            return render(request, 'home/cadastro.html', {'form': form, 'msg': msg})
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

