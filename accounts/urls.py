from django.urls import path
from .views import signup_view, login_view, logout_view
from .views import painel_admin

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("admin-panel/", painel_admin, name="admin_panel"),
]