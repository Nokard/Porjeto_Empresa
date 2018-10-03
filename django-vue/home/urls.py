from django.conf.urls import url
from django.urls import path
from home.views import index
from .views import listarCnpjView


app_name = 'home'
urlpatterns = [
    path('', index, name="index"),
    #path('/home/empresas', empresas, name="empresas"),
    path('CNPJ/<int:pk>/', listarCnpjView.as_view(), name="lista_cnpj"),

]