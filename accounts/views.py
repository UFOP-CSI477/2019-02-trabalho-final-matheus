from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserRegistrationForm
# Create your views here.

def login_user(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
        else:
            messages.error(request,'Login ou Senha incorreto(a)')
    return render(request,'accounts/login.html', {})

def logout_user(request):
    
    logout(request)
    return redirect('home')

def user_registration(request):

    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username,email = email,password = password)
            messages.success(request,'Obrigado por se registrar {}'.format(user.username))
            return redirect('accounts:login')
    
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})