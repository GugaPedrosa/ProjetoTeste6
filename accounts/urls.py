from django.urls import path
from .views import signup_view, login_view, logout_view, painel_admin, cadastrar_filme, cadastrar_livro, home

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("admin-panel/", painel_admin, name="admin_panel"),
    path("cadastrar-filme/", cadastrar_filme, name="cadastrar_filme"),
    path("cadastrar-livro/", cadastrar_livro, name="cadastrar_livro"),
    path('', home, name='home'),
]