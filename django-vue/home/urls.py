from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views 
from home.views import do_logout


app_name = 'home'
urlpatterns = [
    
    path('', views.first, name="first" ),
    path('INDEX/', views.index, name="index"),
    path('', views.pesquisar, name="pesquisar"), 

    path('<int:pk>/', views.listarCnpjView.as_view(), name='emp_detail'),
    
    
    path('LOGIN/', LoginView.as_view(), name='login'),
    path('INDEX/LOGOUT/', do_logout, name='do_logout'), 
    
    #path('CADASTRO/', views.cadastro, name="cadastro"),

]