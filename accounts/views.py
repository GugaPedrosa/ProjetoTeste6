from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import Filme

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

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import FilmeForm, LivroForm

def admin_required(user):
    return user.is_authenticated and user.is_admin

@user_passes_test(admin_required)
def cadastrar_filme(request):
    if request.method == "POST":
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "accounts/sucesso.html", {"mensagem": "Filme cadastrado com sucesso!"})
    else:
        form = FilmeForm()
    return render(request, "accounts/form_filme.html", {"form": form})

def cadastrar_livro(request):
    return render(request, 'accounts/form_html')

@user_passes_test(admin_required)
def home(request):
    genero = request.GET.get('genero', 'Todos')
    if genero == 'Todos':
        filmes = Filme.objects.all()
    else:
        filmes = Filme.objects.filter(genero__iexact=genero)

    return render(request, 'accounts/home.html', {'filmes': filmes, 'genero': genero})




from django.shortcuts import get_object_or_404

def detalhe_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    return render(request, 'accounts/detalhe_filme.html', {'filme': filme})