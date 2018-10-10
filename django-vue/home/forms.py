from .models import AuthUser, HomeUsuarios
from django.forms import ModelForm
from django import forms

                
class Login(ModelForm):
    class Meta:
        model = AuthUser
        fields = ['username','password']


class Usuario_Cadastro(ModelForm):
    
    class Meta:
        model = HomeUsuarios
                
        fields = ['username','nome','email','senha']

        widgets = {

            'username':forms.TextInput(attrs={'placeholder':' Digite seu Usuario'}),

            'nome': forms.TextInput(attrs={'placeholder':' Digite seu nome'}),

            'email': forms.EmailInput(attrs={'placeholder':' Digite seu email'}),

            'senha': forms.PasswordInput(attrs={'placeholder':' Digite sua senha'})

        }