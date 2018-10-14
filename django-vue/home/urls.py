from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views 
from home.views import do_logout
from django.contrib.auth import views as auth_views

app_name = 'home'
urlpatterns = [
    
    path('', views.first, name="first" ),

    path('INDEX/', views.index, name="index"),
    
    path('', views.pesquisar, name="pesquisar"), 

    path('<int:pk>/', views.listarCnpjView.as_view(), name='emp_detail'),
        
    path('LOGIN', LoginView.as_view(), name='login'),

    path('EMAIL', views.validarEmails, name='ValidarEmails'),

    #path('LOGIN', views.do_login, name='login'),

    #path('LOGIN/', LoginView.as_view(), name='login'),
    
    path('LOGOUT', do_logout, name='do_logout'), 
    
    path('REGISTER', views.cadastre,  name="cadastre" ),
    #path('CADASTRO/', views.cadastro, name="cadastro"),

]