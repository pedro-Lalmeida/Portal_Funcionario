from urllib import request

from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'usuarios/home.html'

class PainelView(LoginRequiredMixin, TemplateView):
    template_name = 'usuarios/painel.html'

class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'usuarios/perfil.html'

class Login(LoginView):
    template_name = 'usuarios/login.html'

class Logout(LogoutView):
    template_name = 'usuarios/logout.html'