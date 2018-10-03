from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic.detail import DetailView


from .models import Empresas


def index(request):
    pesquisa = request.GET.get('pesquisa', None)

    if pesquisa:
        Emp = Empresas.objects.filter(doc=pesquisa)
    else:
        Emp = Empresas.objects.all()[:10]
        
    return render(request,'home/index.html',{'Empresas': Emp })


class listarCnpjView(DetailView):
    model = Empresas
