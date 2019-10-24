from django.shortcuts import render, redirect

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()

    else:
        form = CustomUserCreationForm()
        context = {}

def login(request):
    pass

def logout(request):
    pass