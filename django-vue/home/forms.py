from .models import AuthUser
from django.forms import ModelForm
from django import forms


class Register(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['username','email','password']

        #Colocando o campo Senha como MASCARADO
        widgets = {

            'username':forms.TextInput(attrs={'placeholder':' Digite seu Usuario'}),

            'email': forms.EmailInput(attrs={'placeholder':' Digite seu email'}),

            'password': forms.PasswordInput(attrs={'placeholder':' Digite sua senha'})
        }
    
     

                
class Login(ModelForm):
    class Meta:
        model = AuthUser
        fields = ['username','password',]