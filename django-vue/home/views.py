import re
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout


from .models import Empresas


#PAGINA INICIAL
def first(request):
    return render(request, 'home/index.html')

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
        return render(request, 'home/index.html', {'Empresas': emp})


#Funcão para mostrar os detalhes do CNPJ
class listarCnpjView(DetailView):
    model = Empresas
    template_name='home/empresas_detail.html'
    context_object_name = 'emp_detail'

#Funcao para logout
def do_logout(request):
    logout(request)
    