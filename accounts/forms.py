from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Filme, Livro

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_admin = forms.BooleanField(required=False, label="Cadastrar como admin?")

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2", "is_admin"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["is_admin"]:
            user.is_admin = True
            user.is_staff = True
        if commit:
            user.save()
        return user

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'diretor', 'ano', 'sinopse']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano', 'descricao']