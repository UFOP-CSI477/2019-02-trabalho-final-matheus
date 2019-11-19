from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
                                label ='Username', 
                                max_length= 100,
                                widget = forms.TextInput(attrs={'class':'form-control'}),)
    email = forms.EmailField(widget = forms.TextInput(attrs={'class':'form-control'}),)
    password = forms.CharField(
                                label = "Password", 
                                max_length= 100, 
                                min_length= 5,
                                widget = forms.PasswordInput(attrs={'class':'form-control'}),)
    password1 = forms.CharField(
                                label = "Confirm password", 
                                max_length= 100, 
                                min_length= 5,
                                widget = forms.PasswordInput(attrs={'class':'form-control'}),)

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise ValidationError("Email já registrado, digite outro email!")
        return email

    
    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('password1')
        
        if p1 and p2 :
            if p1 != p2: 
                raise ValidationError('As senhas não combinam, tente novamente!')
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Usuário já existe, tente outro usuário!')
        return username