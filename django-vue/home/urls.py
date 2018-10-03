from django.conf.urls import url
from django.urls import path
from home.views import index
from . import views 


app_name = 'home'
urlpatterns = [
    path('', index, name="index"),
    #path('/home/empresas', empresas, name="empresas"),
    path('CNPJ/<int:pk>/', views.listarCnpjView.as_view(), name="lista_cnpj"),
    path('', views.EmpresasList.as_view()),

]