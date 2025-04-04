from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")
from django.contrib.auth.decorators import user_passes_test

def admin_required(user):
    return user.is_admin

@user_passes_test(admin_required)
def painel_admin(request):
    return render(request, "accounts/admin_panel.html")

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def admin_required(user):
    return user.is_authenticated and user.is_admin