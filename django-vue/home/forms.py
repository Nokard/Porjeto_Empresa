from .models import AuthUser, Usuarios
from django.forms import ModelForm
from django import forms

                
class Login(ModelForm):

    class Meta:
        model = AuthUser

        fields = ['username','password']

        widgets = {
        
        'username': forms.TextInput(attrs={'placeholder':' Digite seu Usuario'}),

        'password': forms.PasswordInput(attrs={'placeholder':' Digite sua senha'})

        }


class Usuario_Cadastro(ModelForm):


    class Meta:
        model = AuthUser

        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        widgets = {

                'username': forms.TextInput(attrs={'placeholder': ' Digite seu Usuario'}),

                'first_name': forms.TextInput(attrs={'placeholder': ' Digite seu nome'}),

                'last_name': forms.TextInput(attrs={'placeholder': ' Digite seu ultimo nome'}),

                'email': forms.EmailInput(attrs={'placeholder': ' Digite seu email'}),

                'password': forms.PasswordInput(attrs={'placeholder': ' Digite sua senha'})

            }


        def clean_username(self):
            user = self.cleaned_data['username']
            try:
                match = AuthUser.objects.get(username=user)
            except:
                return self.cleaned_data['username']
            raise forms.ValidationError('Usuario com esse Nick já existe')


        def clean_email(self):
            email_user = self.cleaned_data['email']

            try:
                match = AuthUser.objects.get(email=email_user)
            except:
                return self.cleaned_data['email']
            raise forms.ValidationError('Usuário com esse email já existe ')


        def clean_password(self):

            senha1 = self.cleaned_data['senha']
            senha2 = self.cleaned_data['senha2']

            try:

                if senha1 != senha2:
                    raise forms.ValidationError('Senha diferentes ! tente novamente ')
            except:
                return self.cleaned_data['senha']




'''
class Usuario_Cadastro(ModelForm):
    
    class Meta:
        model = AuthUser
                
        fields = ['username','nome','email','password']

        widgets = {

            'username':forms.TextInput(attrs={'placeholder':' Digite seu Usuario'}),

            'nome': forms.TextInput(attrs={'placeholder':' Digite seu nome'}),

            'email': forms.EmailInput(attrs={'placeholder':' Digite seu email'}),

            'password': forms.PasswordInput(attrs={'placeholder':' Digite sua senha'})

        }

    def clean_username(self):
            user = self.cleaned_data['username']
            try:
                match = Usuarios.objects.get(username = user)
            except:
                return self.cleaned_data['username']
            raise forms.ValidationError('Usuario com esse Nick já existe')

    def clean_email(self):
        email_user = self.cleaned_data['email']

        try:
            match = Usuarios.objects.get(email = email_user)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError('Usuário com esse email já existe ')


        
'''
